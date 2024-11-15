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
