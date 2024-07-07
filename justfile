default:
    @just --list

run:
    npm run dev

build:
    npm run build

format:
    npx prettier --write src/components/  src/pages src/layouts