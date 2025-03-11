import DOMPurify from "dompurify";
import Fuse from "fuse.js";

// Global vars
let searchTerm;

// Selectors
const form = document.querySelector("form");

async function getSearchIndex() {
  try {
    const res = await fetch("/api/blog-posts.json");
    const data = await res.json();
    const searchIndex = data;
    return searchIndex;
  } catch (e) {
    console.error(e);
  }
}

interface SearchIndexInterface {
  title: string;
  description: string;
  tags: string[]
  keywords: string[];
  date: string;
  slug: string;
}

async function doSearch(searchTerm: string) {
  const searchIndex = await getSearchIndex();
  const fuse = new Fuse<SearchIndexInterface>(searchIndex, {
    keys: [
      { name: "title", weight: 2 },
      { name: "description", weight: 1 },
      { name: "tags", weight: 2 },
      { name: "keywords", weight: 3 },
      { name: "date", weight: 1 },
    ],
  });
  const searchResults = fuse.search(searchTerm);

  // Update the page with search results
  const searchResultHTML = document.querySelector<HTMLElement>("#search-results");
  if (searchResultHTML === null) {
    console.error("Search results container not found");
    return;
  }

  // Clear existing results
  searchResultHTML.innerHTML = "";

  // Update the page with search results
  searchResults.forEach((result) => {
    const date = new Date(result.item.date)
    const humanReadableDate = date.toLocaleDateString('en-CA', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });

    // Update with new results
    const li = document.createElement("li");
    li.innerHTML = `
      <div class="pt-4">
        <a href="/blog/${result.item.slug}" class="text-lg font-bold text-primary hover:text-primary hover:drop-shadow-lg hover:underline">
          ${result.item.title}
        </a>
        <div class="text-light text-gray-500">
          ${humanReadableDate}
        </div>
      </div>
    `;
    searchResultHTML.appendChild(li);
  });
}

// -----------------------------------------------------------------------------
// Event listeners
// -----------------------------------------------------------------------------

// Update search box on page load
window.addEventListener("DOMContentLoaded", () => {
  const urlParams = DOMPurify.sanitize(
    new URLSearchParams(window.location.search).get("q") || ""
  );
  const search = document.querySelector("#search") as HTMLInputElement;
  if (search) {
    search.value = urlParams;
    search.focus();
    doSearch(urlParams);
  }
});

// Handle form submission
form?.addEventListener("submit", (e) => {
  // Don't post the form
  e.preventDefault();
  // Parse the form
  const formData = new FormData(form);
  const rawSearchTerm = formData.get("search");
  if (!rawSearchTerm) return;
  searchTerm = DOMPurify.sanitize(rawSearchTerm.toString());
  // Validation of input
  if (!searchTerm || searchTerm.length === 0) return;
  // Update the URL
  const url = new URL("/search", window.location.origin);
  url.searchParams.set("q", searchTerm);
  window.history.replaceState(null, "", url.toString());
  // Search the index
  doSearch(searchTerm);
});