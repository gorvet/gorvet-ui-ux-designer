---
name: gorvet-frontend-seo
description: Implement and review technical frontend SEO for public indexable web pages. Use for crawlability, indexability, semantic document structure, titles/descriptions, canonical URLs, robots directives, social metadata, structured data, internal links, image SEO, localization, rendering, sitemaps, and search-friendly performance.
license: MIT
metadata:
  author: GORVET
---

# Frontend SEO

Apply this skill only where search discovery matters. Private/admin/authenticated application surfaces usually do not need SEO optimization beyond sane semantics and performance.

## First classify the page

Determine whether the page is:

- public and indexable;
- public but intentionally `noindex`;
- authenticated/private;
- duplicate/alternate/canonicalized;
- localized/region-specific.

Do not “SEO optimize” pages that should not be indexed.

## Technical baseline

For indexable pages verify:

- meaningful document `<title>` aligned with page purpose;
- sensible meta description where useful;
- one clear page topic and semantic heading structure;
- crawlable real links (`a href`) for navigation;
- canonical URL when duplicates/variants can exist;
- robots directives consistent with intent;
- indexable content available to search rendering, not hidden behind inaccessible interaction;
- meaningful internal linking and anchor text;
- image dimensions, descriptive alternatives when informative, and appropriate loading strategy;
- correct language/locale signals and `hreflang` when the project actually has alternates;
- sitemap/feed considerations for discoverable URL sets.

## Analyze or defer explicitly

Do not silently omit an SEO item merely because deployment information is missing.

- If the production URL is unknown, do not invent `canonical`, `og:url`, absolute social-image URLs, sitemap locations, or `hreflang` destinations. Mark those decisions as deferred/pending deployment information.
- If a preferred social image does not exist, identify it as a missing asset when social sharing matters rather than fabricating a URL.
- If robots/indexing intent is unclear, determine it from the product/context or flag the ambiguity before publishing behavior that may expose or hide content incorrectly.
- If structured data suitability is uncertain, omit it rather than inventing a schema solely to “complete SEO”; explain the decision when relevant.
- A valid deferral is an explicit decision with a dependency. Silence is not analysis.

## Structured data

Use JSON-LD when suitable and supported by the target search feature. Structured data must describe visible truthful page content; never invent ratings, prices, authors, reviews or entities for rich results. Validate against current search-engine documentation.

## Social metadata

When public sharing matters, implement consistent Open Graph/social preview metadata, including a suitable preferred image. Treat social metadata as sharing UX, not ranking magic.

Use platform-specific metadata only when it adds meaningful compatibility beyond the chosen Open Graph baseline; do not add tags mechanically.

## JavaScript/rendering

Modern search engines can render JavaScript, but critical public content and links should still be reliably discoverable, renderable, performant, and accessible. Respect the project's SSR/SSG/CSR architecture rather than replacing it solely for SEO unless evidence justifies the change.

## Performance

Treat Core Web Vitals and user-perceived performance as quality/search considerations: LCP, INP and CLS are relevant signals, but do not sacrifice product correctness for synthetic-score chasing.

## Boundaries

SEO does not guarantee ranking. Do not keyword-stuff, generate hidden text, fabricate schema, or make unsupported ranking claims.

When framework-specific placement matters (for example meta files, route metadata, server templates), follow any installed adapter's technical contract.
