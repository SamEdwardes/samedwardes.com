# blog-development

[![Netlify Status](https://api.netlify.com/api/v1/badges/f842119c-ee2a-4b18-9658-befe42fe8a2a/deploy-status)](https://app.netlify.com/sites/samedwardes/deploys)

The development repo for my blog [https://samedwardes.com/](https://samedwardes.com/).

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

A change to the README.

### Installation

Install node:

```
$ brew install node
```

Install and enable corepack

```
$ brew install corepack
```

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.
