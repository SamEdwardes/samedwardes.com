preview:
    yarn start

new name:
    mkdir blog/{{name}}
    cp templates/blog-post/index.md blog/{{name}}/index.md

open-netlify:
    open https://app.netlify.com/sites/samedwardes/overview

open-github:
    open https://github.com/SamEdwardes/samedwardes.com

clean:
    rm -rf build
    rm -rf node_modules
    rm yarn.lock