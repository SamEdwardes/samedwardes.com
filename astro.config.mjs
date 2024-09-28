import { defineConfig, envField } from "astro/config";
import tailwind from "@astrojs/tailwind";
import expressiveCode from "astro-expressive-code";
import mdx from "@astrojs/mdx";
import netlify from "@astrojs/netlify";


// https://astro.build/config
export default defineConfig({
  // Basic
  site: "https://samedwardes.com",
  // Integrations
  integrations: [
    tailwind(),
    expressiveCode({
      frames: {
        extractFileNameFromCode: false
      }
    }),
    mdx()],
  // Netlify
  output: "hybrid",
  adapter: netlify(),
  experimental: {
    env: {
      schema: {
        NOTION_TOKEN: envField.string({
          context: "server",
          access: "secret"
        })
      }
    }
  },
  // Redirects
  redirects: {
    // TODO: create replacement pages for these
    '/tags': '/',
    '/projects': '/',
    '/outdoors': '/',
    '/outdoors': '/',
    // Old blog posts paths
    '/2012/09/09/running-pei': '/blog/2012-09-09-running-pei',
    '/2015/06/27/cycling-kingston-to': '/blog/2015-06-27-cycling-kingston-to',
    '/2018/01/01/cycling-portugal': '/blog/2018-01-01-cycling-portugal',
    '/2019/07/17/best-great-lake-surfing-vids': '/blog/2019-07-17-best-great-lake-surfing-vids',
    '/2019/08/22/cycling-canada-main': '/blog/2019-08-22-cycling-canada-main',
    '/2019/08/31/cycling-bc-coast': '/blog/2019-08-31-cycling-bc-coast',
    '/2019/11/15/dash-heroku-cookie-cutter': '/blog/2019-11-15-dash-heroku-cookie-cutter',
    '/2020/01/31/open-ipynb-with-double-click': '/blog/2020-01-31-open-ipynb-with-double-click',
    '/2020/02/08/how-to-open-github-from-cl': '/blog/2020-02-08-how-to-open-github-from-cl',
    '/2020/05/31/is-the-ufc-fair': '/blog/2020-05-31-is-the-ufc-fair',
    '/2020/06/08/datascience-setup': '/blog/2020-06-08-datascience-setup',
    '/2022/01/31/how-to-learn-r': '/blog/2022-01-31-how-to-learn-r',
    '/2022/02/15/data-science-setup-mac': '/blog/2022-02-15-data-science-setup-mac',
    '/2022/03/18/fastapi-beanie-one-page': '/blog/2022-03-18-fastapi-beanie-one-page',
    '/2022/04/14/fastapi-webapp-with-auth': '/blog/2022-04-14-fastapi-webapp-with-auth',
    '/2022/04/19/how-to-learn-python-for-ds': '/blog/2022-04-19-how-to-learn-python-for-ds',
    '/2022/07/14/pulumi-with-jinja-templates': '/blog/2022-07-14-pulumi-with-jinja-templates',
    '/2022/10/23/best-jupyter-lab-install': '/blog/2022-10-23-best-jupyter-lab-install',
    '/2022/10/27/full-gh-code-review': '/blog/2022-10-27-full-gh-code-review',
    '/2023/01/09/new-linux-user-with-passwor': '/blog/2023-01-09-new-linux-user-with-passwor',
    '/2023/02/13/kubectl-exec-pro-tip': '/blog/2023-02-13-kubectl-exec-pro-tip',
    '/2023/03/19/pycascades-2023-lightning-talk': '/blog/2023-03-19-pycascades-2023-lightning-talk',
    '/2023/04/14/how-to-learn-kubernetes': '/blog/2023-04-14-how-to-learn-kubernetes',
    '/2023/04/15/get-server-info': '/blog/2023-04-15-get-server-info',
    '/2023/04/28/blogging-with-docusaurus-and-quarto': '/blog/2023-04-28-blogging-with-docusaurus-and-quarto',
    '/2023/06/11/vscode-bash-to-terminal': '/blog/2023-06-11-vscode-bash-to-terminal',
    '/2023/07/13/use-pyenv-with-reticulate': '/blog/2023-07-13-use-pyenv-with-reticulate',
    '/2023/08/19/k8s-ingress-to-external-service': '/blog/2023-08-19-k8s-ingress-to-external-service',
    '/2023/10/12/fixing-renv-numpy-issues': '/blog/2023-10-12-fixing-renv-numpy-issues',
    '/2023/11/03/1password-for-secret-dotfiles': '/blog/2023-11-03-1password-for-secret-dotfiles',
    '/2023/11/19/homelab-tls-with-caddy-and-cloudflare': '/blog/2023-11-19-homelab-tls-with-caddy-and-cloudflare',
    '/2023/11/28/1password-for-secret-dotfiles-update': '/blog/2023-11-28-1password-for-secret-dotfiles-update',
    '/2024/01/09/requirements-txt-workflow-for-new-project': '/blog/2024-01-09-requirements-txt-workflow-for-new-project',
    '/2024/04/21/python-uv-workflow': '/blog/2024-04-21-python-uv-workflow'
  }
});