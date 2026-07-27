# Northern England SEO rollout

Date: 2026-07-27

## Direction

TreeFellingNearMe is now a Northern England service hub rather than a Great Britain page. The architecture follows search intent:

- Homepage: service-led Northern England hub
- City pages: `/<city>/`
- Future city/service pages: `/<city>/<service>/`, added only when Search Console impressions justify them

The first batch deliberately stops at ten city pages. Publishing dozens of near-identical pages at once would weaken quality and make the site look like a doorway-page network.

## First ten cities

UK keyword demand checked through OpenSEO/DataForSEO for `tree surgeon [city]`:

| City | Monthly UK searches |
|---|---:|
| Manchester | 590 |
| Leeds | 480 |
| Liverpool | 480 |
| Sheffield | 480 |
| Newcastle | 390 |
| Preston | 260 |
| York | 210 |
| Sunderland | 140 |
| Durham | 110 |
| Carlisle | 110 |

`Tree surgeon [city]` is used as the city-page primary target because it is the dominant commercial local intent. Tree felling, tree removal, stump grinding and emergency work remain the service focus of each page.

## SERP and competitor findings

OpenSEO SERPs and competitor keyword data showed repeated demand around:

- tree felling near me
- tree removal near me
- tree surgeon near me
- tree cutting service
- tree and stump removal
- emergency tree removal
- stump grinding
- tree felling cost
- tree removal cost
- sectional dismantling

These terms were incorporated where they match the reader's job. They were not repeated mechanically.

The strongest local results combine:

- exact city relevance in title and H1
- clear service coverage
- insurance and qualification proof
- free quote or inspection CTA
- emergency-work language
- stump grinding and removal options
- local access, council and conservation-area context
- nearby service areas

Treemend's city-page footprint confirms that scalable location architecture can rank, but its pages are broad and repetitive. The implementation here uses shared structure with city-specific access, tree, authority and nearby-area content.

## Implemented

- Northern England homepage title, description, H1, schema and coverage language
- Homepage links to all ten city pages
- Southern England, Scotland and Wales targeting removed
- Southern testimonials removed from the visible review set
- Ten indexable city pages with unique metadata, H1s and local content
- Service, WebPage and breadcrumb JSON-LD on city pages
- Internal links between city pages and back to the homepage enquiry form
- Expanded sitemap with all eleven URLs
- Static validation for titles, descriptions, H1s, schema, links, word counts and sitemap coverage

## Next evidence gate

Do not create all city/subservice combinations now. Review Search Console after indexing. Add a page such as `/manchester/tree-removal/` only when the parent city page records meaningful impressions for that service and the subpage can carry genuinely specific content.
