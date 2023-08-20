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
  projectName: 'samedwardes.com', // Usually your repo name.
  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: 'homelab',
          routeBasePath: 'homelab',
          sidebarPath: require.resolve('./sidebarsHomelab.js'),
        },
        blog: {
          routeBasePath: '/', // Serve the blog at the site's root
          blogTitle: 'Blog',
          blogDescription: 'Sam Edwardes personal blog',
          postsPerPage: 'ALL',
          showReadingTime: true,
          // blogSidebarTitle: 'All posts',
          blogSidebarCount: 0,
          editUrl: 'https://github.com/SamEdwardes/samedwardes.com/tree/main/',
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
        title: "Sam's Blog",
        logo: {
          alt: 'logo',
          src: 'img/profile.png',
        },
        items: [
          {to: '/', label: 'Blog', position: 'left'},
          {to: '/tags', label: 'Tags', position: 'left'},
          {to: '/projects', label: 'Projects', position: 'left'},
          {to: '/outdoors', label: 'Outdoors', position: 'left'},
          {to: '/homelab', label: 'Homelab', position: 'left'},
          {to: '/about', label: 'About', position: 'left'},
          {
            href: 'https://github.com/SamEdwardes/samedwardes.com',
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
                href: 'https://www.youtube.com/channel/UCkXD_pR2bYGOyf8Eh6T_BNw',
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
        copyright: `Copyright © ${new Date().getFullYear()} Sam Edwardes. Built with Docusaurus.`,
      },
      prism: {
        theme: lightCodeTheme,
        darkTheme: darkCodeTheme,
      },
    }),
    plugins: [
      [
        '@docusaurus/plugin-content-docs',
        {
          id: 'test',
          path: 'test',
          routeBasePath: 'test',
          sidebarPath: require.resolve('./sidebarsTest.js'),
          // ... other options
        },
      ],
      [
        '@docusaurus/plugin-ideal-image',
        {
          quality: 70,
          max: 1030, // max resized image's size.
          min: 640, // min resized image's size. if original is lower, use that size.
          steps: 2, // the max number of images generated between min and max (inclusive)
          disableInDev: false,
        }
      ],
      // [
      //   '@docusaurus/plugin-client-redirects', {
      //     redirects: [
      //       {
      //         to: "/projects",
      //         from: "/data-science"
      //       }
      //     ]
      //   }
      // ]
    ]
};

module.exports = config;
