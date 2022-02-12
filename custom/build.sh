#!/bin/bash
#
# This simple bash script utilizes the swagger-codegen container to generate an
# API-client for python from Contabo's API documentation.
#
set -e

git_user_id=p-fruck
git_repo_id=python-contabo
proj_dir="$(readlink -f $(dirname $0))/.." # root directory of the project

function customize_readme() {
    mv README.md README.md.gen
    # apply custom introduction to README.md
    cp custom/README.md.part README.md
    # get line number of the requirements heading
    line=$(grep -n '## Getting Started' README.md.gen | cut -d ':' -f 1 | tail -1)
    # add requirements and documentation to README.md
    tail -n+${line} README.md.gen >> README.md
    rm README.md.gen
}

# by default, the Contabo API documentation is set as package description for the PyPI package.
# Instead, the GitHub README should be defined as description.
function customize_pypi_description() {
    line_no=$(grep -n 'long_description' setup.py | cut -d ':' -f 1)
    head -n ${line_no} setup.py > setup.py.new

    # add README content with absolute links to GitHub repo
    sed "s#(docs/#(https://github.com/${git_user_id}/${git_repo_id}/blob/main/docs/#g" README.md >> setup.py.new

    # add additional metadata
    cat << EOF >> setup.py.new
    """,
    long_description_content_type='text/markdown',
    project_urls={
        "Bug Tracker": "https://github.com/${git_user_id}/${git_repo_id}/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
)
EOF

    mv setup.py.new setup.py

    # replace default description with a custom one and escape linebreaks in codeblocks
    sed -i \
        -e 's;    description=.*;    description="This is an UNOFFICIAL Python API client for Contabo",;g' \
        -e 's/\\n/\\\\n/g' \
        setup.py

    # validate syntax
    python -m py_compile setup.py
}

if command -v podman >/dev/null 2>&1; then
    cmd="podman"
else
    cmd="docker"
fi

$cmd run --rm \
    -v "${proj_dir}":/local:Z \
    swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://api.contabo.com/api-v1.yaml \
    -l python \
    --git-user-id ${git_user_id} \
    --git-repo-id ${git_repo_id} \
    -o /local/ \
    -c /local/custom/config.json

cd "${proj_dir}"

# Contabo does not declare attributes as nullable, so I have to catch them manually
sed -i 's/^\(\s\+\)self\.\([a-z][a-z_]\+\) = \2$/\1if \2 is not None:\n\1    self.\2 = \2/g' pfruck_contabo/models/*_response{,_data}.py

# Remove Contabo API Documentation from sourcefiles
find . -name "*.py" -exec sed -i '/^\s\+# Introduction .*$/d' {} \;

# apply custom patches to source files
for patchfile in $(find custom/patches -type f)
do
    patch -p0 < "${patchfile}"
done

# No functionality in unit-tests, they just validate that all files have valid syntax :)
python -m unittest

customize_readme

customize_pypi_description
