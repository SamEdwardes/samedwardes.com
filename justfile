# List all of the commands
default:
    @just --list

# bun run dev
run:
    bun run dev

# bun run build
build:
    bun run build

# bunx prettier
format:
    bunx prettier --write src/components src/pages src/layouts

pre-commit:
    just format

# Create the template for a new blog post
new title:
    #!/usr/bin/env bash
    mkdir -p src/content/blog/{{title}}
    tee src/content/blog/{{title}}/index.mdx <<EOF
    ---
    title: $( echo {{title}} | cut -c12-)
    description:
    author: Sam Edwardes
    date: $(echo {{title}} | cut -c1-10)
    tags:
    - tools
    - python
    - r
    - quarto
    - outdoors
    - blog
    - astro
    - data
    - linux
    - command line
    - homelab
    - infrastructure
    ---
    EOF
