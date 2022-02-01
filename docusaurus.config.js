// @ts-check
// Note: type annotations allow type checking and IDEs autocompletion

const lightCodeTheme = require('prism-react-renderer/themes/github');
const darkCodeTheme = require('prism-react-renderer/themes/dracula');

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Sam Edwardes',
  tagline: 'The personal blog of Sam Edwardes',
  url: 'https://samedwardes.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'SamEdwardes', // Usually your GitHub org/user name.
  projectName: 'personal-blog', // Usually your repo name.

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: false,
        blog: {
          routeBasePath: '/', // Serve the blog at the site's root
          blogTitle: 'Blog',
          blogDescription: 'Sam Edwardes personal blog',
          postsPerPage: 'ALL',
          showReadingTime: true,
          // blogSidebarTitle: 'All posts',
          blogSidebarCount: 0,
          editUrl: 'https://github.com/SamEdwardes/personal-blog/tree/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        title: 'Sam Edwardes',
        logo: {
          alt: 'Sam I Am Circle Picture',
          src: 'img/profile.png',
        },
        items: [
          {to: '/', label: 'Blog', position: 'left'},
          {to: '/data-science', label: 'Data Science', position: 'left'},
          {to: '/outdoors', label: 'Outdoors', position: 'left'},
          // {type: 'doc', docId: 'intro', position: 'left', label: 'Other Stuff',},
          {to: '/about', label: 'About', position: 'left'},
          {
            href: 'https://github.com/SamEdwardes/personal-blog',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Socials',
            items: [
              {
                label: 'Twitter',
                href: 'https://twitter.com/TheReaLSamlam',
              },
              {
                label: 'YouTube',
                href: 'https://www.linkedin.com/in/samedwardes/',
              },
              {
                label: 'LinkedIn',
                href: 'https://www.linkedin.com/in/samedwardes/',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/SamEdwardes',
              },
              {
                label: 'Email',
                href: 'mailto:edwardes.s@gmail.com',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
};

module.exports = config;
