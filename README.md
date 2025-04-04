# samedwardes.com

<a href="https://app.netlify.com/sites/samedwardes/deploys" target="_blank"><img src="https://api.netlify.com/api/v1/badges/f842119c-ee2a-4b18-9658-befe42fe8a2a/deploy-status" alt="Netlify status"/></a>

The development repo for my blog [https://samedwardes.com/](https://samedwardes.com/).

![Screenshot of Blog](public/images/screenshot-of-blog.png)

## Development

### Pre-commit

Copy the code below to `.git/hooks/pre-commit` and make it executable with `chmod +x .git/hooks/pre-commit`.

```bash
#!/usr/bin/env bash
# ^ Note the above "shebang" line. This says "This is an executable shell script"
# Name this script "pre-commit" and place it in the ".git/hooks/" directory

# If any command fails, exit immediately with that command's exit status
set -eo pipefail

# Run commands
just pre-commit
```

## Astro

```sh
npm create astro@latest -- --template minimal
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/minimal)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/minimal)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/minimal/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

### 🚀 Project Structure

Inside of your Astro project, you'll see the following folders and files:

```text
/
├── public/
├── src/
│   └── pages/
│       └── index.astro
└── package.json
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.

### 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

### 👀 Want to learn more?

Feel free to check [our documentation](https://docs.astro.build) or jump into our [Discord server](https://astro.build/chat).
