/// <reference path="../.astro/env.d.ts" />
/// <reference path="../.astro/types.d.ts" />
/// <reference types="astro/client" />

// @alpinejs/ui ships no type declarations and has no @types package.
declare module "@alpinejs/ui" {
  import type { PluginCallback } from "alpinejs";
  const ui: PluginCallback;
  export default ui;
}

interface Window {
  Alpine: import("alpinejs").Alpine;
  htmx: typeof import("htmx.org").default;
}
