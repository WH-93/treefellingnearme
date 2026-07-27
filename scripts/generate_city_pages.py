#!/usr/bin/env python3
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
PHONE_DISPLAY = "07503 512953"
PHONE_LINK = "07503512953"
BASE = "https://treefellingnearme.co.uk"

CITIES = [
    {
        "slug": "manchester", "city": "Manchester", "region": "Greater Manchester",
        "volume": 590,
        "areas": ["Salford", "Stockport", "Didsbury", "Trafford", "Rochdale", "Oldham"],
        "context": "Manchester jobs range from trees in narrow terraced gardens to mature specimens beside offices, schools and managed estates. Rear access, parked vehicles, extensions and shared boundaries often decide whether a tree can be felled in one piece or needs to be dismantled section by section.",
        "local": "Greater Manchester has ten local authorities, so the council responsible for a Tree Preservation Order or conservation area check depends on the exact address. Send the postcode with your enquiry and the correct local records can be checked before work is arranged.",
        "species": "Mature sycamore, lime, beech and ash are common enquiries across Greater Manchester. Ash dieback and storm damage can make removal urgent, but the condition and safe method still need assessing on site."
    },
    {
        "slug": "leeds", "city": "Leeds", "region": "West Yorkshire",
        "volume": 480,
        "areas": ["Bradford", "Wakefield", "Pudsey", "Morley", "Horsforth", "Roundhay"],
        "context": "Leeds combines dense inner-city streets with larger suburban gardens and commercial grounds. Stone walls, narrow side passages, sloping gardens and neighbouring properties can rule out straight felling even when the tree itself is not especially large.",
        "local": "Leeds has numerous conservation areas and protected trees. The legal check is separate from the physical work, and it should happen before a date is booked. Photos, the postcode and any council correspondence help establish what is needed.",
        "species": "Beech, sycamore, conifer, willow and ash account for many local removal enquiries. The reason may be disease, excessive size, root damage, storm movement or a tree growing too close to a building."
    },
    {
        "slug": "liverpool", "city": "Liverpool", "region": "Merseyside",
        "volume": 480,
        "areas": ["Bootle", "Huyton", "Crosby", "Knowsley", "Allerton", "Widnes"],
        "context": "In Liverpool and across Merseyside, tree removal often means working around terraced properties, rear alleys, boundary walls and limited vehicle access. Coastal winds can also expose weak unions and damaged limbs after bad weather.",
        "local": "Liverpool City Council and neighbouring Merseyside authorities maintain their own conservation area and protected-tree records. The exact address matters. A postcode check avoids making assumptions about which authority or restriction applies.",
        "species": "Large conifers, sycamore, poplar, willow and storm-damaged garden trees are regular reasons people seek a tree surgeon in Liverpool. The safest removal method depends on the drop zone and what sits beneath the crown."
    },
    {
        "slug": "sheffield", "city": "Sheffield", "region": "South Yorkshire",
        "volume": 480,
        "areas": ["Rotherham", "Barnsley", "Hillsborough", "Ecclesall", "Dronfield", "Chapeltown"],
        "context": "Sheffield's hills, stone boundaries and stepped gardens create access problems that do not show up in a photograph of the tree alone. A climber may need to lower timber in controlled sections where slopes, walls or neighbouring roofs remove the normal drop zone.",
        "local": "Sheffield contains many conservation areas and protected trees. If consent is needed, the application should describe the proposed work accurately. The site visit establishes whether removal is justified and whether a different operation may be more appropriate.",
        "species": "Mature beech, sycamore, ash and conifers feature heavily in Sheffield tree work. Trees affected by decay, ash dieback or storm damage need a condition-led assessment rather than a blanket recommendation."
    },
    {
        "slug": "newcastle", "city": "Newcastle", "region": "Tyne and Wear",
        "volume": 390,
        "areas": ["Gateshead", "Gosforth", "Jesmond", "Wallsend", "North Shields", "South Shields"],
        "context": "Newcastle tree work ranges from tight urban gardens in Jesmond and Gosforth to larger sites across Gateshead and North Tyneside. Roads, footpaths, extensions and neighbouring gardens often mean sectional dismantling is safer than dropping the tree whole.",
        "local": "Newcastle, Gateshead and the surrounding Tyne and Wear authorities each handle protected trees and conservation areas within their boundaries. The postcode identifies the correct authority and records before the job proceeds.",
        "species": "Sycamore, ash, lime, willow and large conifers are common removal enquiries around Newcastle. Storm damage and ash dieback are frequent concerns, especially where a tree can reach a house, road or public path."
    },
    {
        "slug": "preston", "city": "Preston", "region": "Lancashire",
        "volume": 260,
        "areas": ["Leyland", "Chorley", "Fulwood", "Penwortham", "Garstang", "Bamber Bridge"],
        "context": "Preston and central Lancashire include compact suburban plots, rural properties and exposed sites. Soft ground, narrow drives and overhead services can affect machinery access, timber handling and the final price as much as the height of the tree.",
        "local": "Protected-tree and conservation-area checks may sit with Preston, South Ribble, Chorley or another Lancashire authority depending on the address. Send the full postcode so the relevant local position can be confirmed.",
        "species": "Conifers, poplar, willow, ash and mature garden trees are common across Preston. Wet ground and wind exposure can reveal root movement or structural weakness that needs inspecting before removal is planned."
    },
    {
        "slug": "york", "city": "York", "region": "North Yorkshire",
        "volume": 210,
        "areas": ["Haxby", "Selby", "Tadcaster", "Easingwold", "Pocklington", "Acomb"],
        "context": "York has historic streets, conservation areas, mature gardens and villages where access can be more restrictive than the tree height suggests. Walls, outbuildings, overhead lines and neighbouring land all influence the felling plan.",
        "local": "York contains protected trees and many conservation areas. Work should not start until the relevant status is checked. Outside the city boundary, a different North Yorkshire authority may apply, so the postcode is essential.",
        "species": "Lime, beech, sycamore, ash and large conifers generate many York tree enquiries. Some need full removal, while others need deadwood or unstable sections made safe without taking down the whole tree."
    },
    {
        "slug": "sunderland", "city": "Sunderland", "region": "Tyne and Wear",
        "volume": 140,
        "areas": ["Washington", "Houghton-le-Spring", "Seaham", "South Shields", "Peterlee", "Hetton-le-Hole"],
        "context": "Sunderland's coastal exposure can turn weak limbs and unstable trees into urgent problems after storms. In built-up areas, close boundaries, conservatories, sheds and public paths usually make controlled dismantling the practical option.",
        "local": "The responsible authority may be Sunderland, Durham or South Tyneside depending on the postcode. Protected-tree and conservation-area checks must be made against the correct local records before work starts.",
        "species": "Ash, sycamore, willow, poplar and conifers are regular Sunderland enquiries. Wind exposure, decay and ash dieback can all affect the safe working method and how quickly the site should be inspected."
    },
    {
        "slug": "durham", "city": "Durham", "region": "County Durham",
        "volume": 110,
        "areas": ["Chester-le-Street", "Consett", "Bishop Auckland", "Spennymoor", "Stanley", "Peterlee"],
        "context": "Durham work covers city gardens, former mining villages, rural properties and commercial sites. Slopes, stone walls, narrow lanes and long carries from the tree to the chipper can substantially change the method and labour involved.",
        "local": "Durham County Council maintains conservation-area and protected-tree records across a wide area. The postcode, photographs and any existing council correspondence help establish the legal position before the job is scheduled.",
        "species": "Ash dieback is a significant concern across County Durham, alongside mature sycamore, beech, willow and conifers. Affected trees need inspecting for condition, access and the safest direction of work."
    },
    {
        "slug": "carlisle", "city": "Carlisle", "region": "Cumbria",
        "volume": 110,
        "areas": ["Brampton", "Penrith", "Wigton", "Longtown", "Dalston", "Gretna"],
        "context": "Carlisle and north Cumbria include exposed gardens, farms, estates and roadside trees. Wind damage, soft ground and distance from hardstanding can affect whether climbing, rigging, machinery or traffic management is required.",
        "local": "Carlisle now sits within Cumberland Council's area. Conservation areas, Tree Preservation Orders and highway constraints still depend on the exact site. The postcode and clear photos help identify the checks required.",
        "species": "Ash, beech, sycamore, conifer and storm-damaged roadside trees are common Carlisle enquiries. Rural space may allow straight felling, but buildings, roads, livestock and overhead services can still require sectional work."
    }
]


def page(city):
    name = city["city"]
    slug = city["slug"]
    region = city["region"]
    url = f"{BASE}/{slug}/"
    title = f"Tree Surgeon {name} | Tree Felling & Removal Near You"
    description = f"Need a tree surgeon in {name}? Tree felling, removal, stump grinding and emergency work across {region}. Free inspection and written quote."
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {"@type": "WebPage", "@id": url, "url": url, "name": title, "description": description, "isPartOf": {"@id": f"{BASE}/#website"}},
            {"@type": "Service", "@id": f"{url}#service", "name": f"Tree felling and removal in {name}", "serviceType": "Tree felling and tree removal", "areaServed": {"@type": "City", "name": name}, "provider": {"@id": f"{BASE}/#organization"}},
            {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
                {"@type": "ListItem", "position": 2, "name": name, "item": url}
            ]}
        ]
    }
    areas = "".join(f"<span>{escape(a)}</span>" for a in city["areas"])
    other = "".join(f'<a href="/{c["slug"]}/">{escape(c["city"])}</a>' for c in CITIES if c["slug"] != slug)
    return f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(description)}">
<link rel="icon" type="image/png" href="/mascot.png">
<meta name="robots" content="index, follow"><link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:title" content="{escape(title)}"><meta property="og:description" content="{escape(description)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/mascot.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet"><link rel="stylesheet" href="/city.css">
<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>
</head>
<body>
<header class="header"><div class="container"><a class="brand" href="/"><img src="/mascot.png" alt="" width="42" height="42"><span>TreeFelling<span>NearMe</span></span></a><a class="phone" href="tel:{PHONE_LINK}">Free quote: {PHONE_DISPLAY}</a></div></header>
<main>
<section class="hero"><div class="container"><nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / {escape(name)}</nav><span class="eyebrow">{escape(region)}</span><h1>Tree Surgeon {escape(name)}</h1><p>Need a tree felled, removed or made safe? Tell us where it is, what is nearby and whether access is restricted. We arrange the inspection and written quote with a qualified, insured tree surgeon covering {escape(name)} and the surrounding area.</p><div class="hero-actions"><a class="btn btn-main" href="/#contact">Get a free inspection</a><a class="btn btn-alt" href="tel:{PHONE_LINK}">Call {PHONE_DISPLAY}</a></div></div></section>
<div class="trust"><div class="container"><span>✓ Qualified tree surgeons</span><span>✓ Public liability insured</span><span>✓ Written quote</span><span>✓ Waste options agreed first</span></div></div>
<section class="section"><div class="container"><h2>Tree felling and removal in {escape(name)}</h2><p class="lead">Straight felling where space allows. Controlled sectional dismantling where it does not. The method is chosen around the tree, access and everything that must be protected below.</p><div class="grid"><article class="card"><h3>Tree felling</h3><p>Dead, diseased, dangerous or unwanted trees brought down safely. A straight fell may work on an open site. Tight gardens usually need the crown and stem removed in sections.</p></article><article class="card"><h3>Tree removal</h3><p>The tree is dismantled, timber cut and branches chipped. Tell us whether you want logs left for firewood or all arisings taken away.</p></article><article class="card"><h3>Stump grinding</h3><p>Tree and stump removal can be included in one quote. Grinding clears the main stump below ground level so the area can be reused or replanted.</p></article><article class="card"><h3>Emergency tree work</h3><p>Fallen trees, hanging limbs and storm damage assessed for urgency. Immediate hazards are prioritised and availability is confirmed before anyone travels.</p></article><article class="card"><h3>Tree cutting service</h3><p>Not every enquiry needs full removal. A tree surgeon can assess whether reduction, deadwood removal or another operation solves the problem with less work.</p></article><article class="card"><h3>Commercial clearance</h3><p>Tree felling and vegetation clearance for managed estates, development sites, schools, landlords and commercial grounds across {escape(region)}.</p></article></div></div></section>
<section class="section alt"><div class="container split"><div class="prose"><h2>What changes the job in {escape(name)}</h2><p>{escape(city["context"])}</p><p>{escape(city["species"])}</p><p>A useful quote needs more than the species and height. Include photographs of the whole tree, its base, the route from the road and anything beneath the branches. That gives the tree surgeon a better first view of the labour and equipment involved.</p></div><aside class="area-box"><h3>Areas around {escape(name)}</h3><p>Coverage includes the city and nearby parts of {escape(region)}, subject to availability and the equipment required.</p><div class="area-list">{areas}</div></aside></div></section>
<section class="section"><div class="container split"><div class="prose"><h2>Tree felling cost in {escape(name)}</h2><p>There is no honest fixed price without seeing the tree and access. Tree removal cost changes with the safe method, crew time, machinery, disposal and whether the stump is included.</p><ul class="cost-list"><li>Tree height, trunk diameter and condition</li><li>Distance from buildings, roads, power lines and boundaries</li><li>Whether straight felling or sectional dismantling is required</li><li>Access for a chipper, stump grinder, platform or crane</li><li>Keeping or removing timber, logs and wood chip</li><li>Stump grinding, traffic management or emergency attendance</li></ul><p>Send the postcode and photos for a free inspection and written quote. You will know what is included before work starts.</p></div><div class="prose"><h2>Permission and local checks</h2><p>{escape(city["local"])}</p><p>A Tree Preservation Order, conservation area or felling licence can affect whether work needs consent. Nesting birds and protected wildlife must also be considered. The relevant checks happen before anybody picks up a saw.</p></div></div></section>
<section class="section alt faq"><div class="container"><h2>Questions about tree removal in {escape(name)}</h2><details><summary>How quickly can somebody inspect the tree?</summary><p>That depends on location, urgency and current availability. Send the postcode, photos and a short description. A fallen tree blocking access is treated differently from planned removal.</p></details><details><summary>Will the stump be removed too?</summary><p>Only if stump grinding is included in the written quote. Ask for tree and stump removal when you enquire so the right machinery can be planned.</p></details><details><summary>What happens to the wood and branches?</summary><p>Branches are normally chipped. Timber can be removed or cut into manageable logs for you to keep. Agree the waste plan before accepting the quote.</p></details><details><summary>Can a tree be removed from a small rear garden?</summary><p>Usually, but restricted access changes the method and cost. Sectional dismantling and controlled lowering are used where there is no safe space to fell the tree whole.</p></details><details><summary>Do I need a tree surgeon or an arborist?</summary><p>For practical felling, removal and climbing work, people usually search for a tree surgeon. Arborist is the broader professional term. The important checks are competence for the operation and suitable insurance.</p></details></div></section>
<section class="section"><div class="container"><h2>Tree surgeons across Northern England</h2><p class="lead">Looking outside {escape(name)}? Start with the city page nearest the tree.</p><div class="city-links">{other}</div></div></section>
<section class="cta"><div class="container"><h2>Tell us about the tree</h2><p>Send the postcode, a few photos and what you need doing. We will arrange the inspection and written quote with a qualified, insured tree surgeon covering {escape(name)}.</p><a class="btn btn-main" href="/#contact">Send an enquiry</a> <a class="btn btn-alt" href="tel:{PHONE_LINK}">Call {PHONE_DISPLAY}</a></div></section>
</main>
<footer class="footer"><div class="container"><p><a href="/">TreeFellingNearMe.co.uk</a> | Tree felling and removal across Northern England</p><p>© 2026 TreeFellingNearMe.co.uk</p></div></footer><a class="mobile-call" href="tel:{PHONE_LINK}">Call for a free quote: {PHONE_DISPLAY}</a>
</body></html>'''


def main():
    for city in CITIES:
        target = ROOT / city["slug"] / "index.html"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(page(city), encoding="utf-8")
    print(f"Generated {len(CITIES)} city pages")

if __name__ == "__main__":
    main()
