local util = require("util")

local biomes = {}

local biome_settings = {
    ["dirt-aubergine"] = "mineral-aubergine-dirt-",
    ["dirt-beige"] = "mineral-beige-dirt-",
    ["dirt-black"] = "mineral-black-dirt-",
    ["dirt-brown"] = "mineral-brown-dirt-",
    ["dirt-cream"] = "mineral-cream-dirt-",
    ["dirt-dustyrose"] = "mineral-dustyrose-dirt-",
    ["dirt-grey"] = "mineral-grey-dirt-",
    ["dirt-purple"] = "mineral-purple-dirt-",
    ["dirt-red"] = "mineral-red-dirt-",
    ["dirt-tan"] = "mineral-tan-dirt-",
    ["dirt-violet"] = "mineral-violet-dirt-",
    ["dirt-white"] = "mineral-white-dirt-",

    ["frozen-snow"] = "frozen-snow-",
    ["frozen-ice"] = "frozen-ice-",

    ["grass-blue"] = "vegetation-blue-grass-",
    ["grass-green"] = "vegetation-green-grass-",
    ["grass-mauve"] = "vegetation-mauve-grass-",
    ["grass-olive"] = "vegetation-olive-grass-",
    ["grass-orange"] = "vegetation-orange-grass-",
    ["grass-purple"] = "vegetation-purple-grass-",
    ["grass-red"] = "vegetation-red-grass-",
    ["grass-turquoise"] = "vegetation-turquoise-grass-",
    ["grass-violet"] = "vegetation-violet-grass-",
    ["grass-yellow"] = "vegetation-yellow-grass-",

    ["sand-aubergine"] = "mineral-aubergine-sand-",
    ["sand-beige"] = "mineral-beige-sand-",
    ["sand-black"] = "mineral-black-sand-",
    ["sand-brown"] = "mineral-brown-sand-",
    ["sand-cream"] = "mineral-cream-sand-",
    ["sand-dustyrose"] = "mineral-dustyrose-sand-",
    ["sand-grey"] = "mineral-grey-sand-",
    ["sand-purple"] = "mineral-purple-sand-",
    ["sand-red"] = "mineral-red-sand-",
    ["sand-tan"] = "mineral-tan-sand-",
    ["sand-violet"] = "mineral-violet-sand-",
    ["sand-white"] = "mineral-white-sand-",

    ["volcanic-blue"] = "volcanic-blue-heat-",
    ["volcanic-green"] = "volcanic-green-heat-",
    ["volcanic-orange"] = "volcanic-orange-heat-",
    ["volcanic-purple"] = "volcanic-purple-heat-",
    ["water-normal"] = "water-normal",
    ["water-deep"] = "water-deep",
    ["water-shallow"] = "water-shallow",
    ["water-mud"] = "water-mud",
}

biomes.biome_settings=biome_settings

local biomes_used = {}

biomes.biomes_used=biomes_used

local tile_alias = util.deepcopy(alien_biomes.tile_alias)
tile_alias["water"] = "water-normal"
tile_alias["deepwater"] = "water-deep"
tile_alias["water-green"] = "water-normal-green"
tile_alias["deepwater-green"] = "water-deep-green"
tile_alias["frozen-snow-5"] = "frozen-ice-5"
tile_alias["frozen-snow-6"] = "frozen-ice-6"
tile_alias["frozen-snow-7"] = "frozen-ice-7"
tile_alias["frozen-snow-8"] = "frozen-ice-8"
tile_alias["frozen-snow-9"] = "frozen-ice-9"

biomes.tile_alias=tile_alias

local dynamic_ranges = {
    ["deepwater"] = { -1e72, 10000 },
    ["water"] = { -1e72, 1e58 },
    ["mud"] = { -10000, 1 },
    ["heat"] = { -10000, 1 },
    ["tile"] = { -10000, 100 },
    ["shallow"] = { -1e72, 10000 },
}

biomes.dynamic_ranges=dynamic_ranges

return biomes
