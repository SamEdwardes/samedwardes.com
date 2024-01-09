default:
 @just --list

preview:
    yarn start

new dirName:
    mkdir blog/{{dirName}}
    cp templates/blog-post/index.md blog/{{dirName}}/index.md
    code blog/{{dirName}}/index.md

open-netlify:
    open https://app.netlify.com/sites/samedwardes/overview

open-github:
    open https://github.com/SamEdwardes/samedwardes.com

clean:
    rm -rf build
    rm -rf node_modules
    rm yarn.lock