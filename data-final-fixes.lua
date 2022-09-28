log("HELLO")

local biome_settings = {
   ["dirt-aubergine"]="mineral-aubergine-dirt-",
   ["dirt-beige"]="mineral-beige-dirt-",
   ["dirt-black"]="mineral-black-dirt-",
   ["dirt-brown"]="mineral-brown-dirt-",
   ["dirt-cream"]="mineral-cream-dirt-",
   ["dirt-dustyrose"]="mineral-dustyrose-dirt-",
   ["dirt-grey"]="mineral-grey-dirt-",
   ["dirt-purple"]="mineral-purple-dirt-",
   ["dirt-red"]="mineral-red-dirt-",
   ["dirt-tan"]="mineral-tan-dirt-",
   ["dirt-violet"]="mineral-violet-dirt-",
   ["dirt-white"]="mineral-white-dirt-",

   ["frozen"]="frozen-snow-",

   ["grass-blue"]="vegetation-blue-grass-",
   ["grass-green"]="vegetation-green-grass-",
   ["grass-mauve"]="vegetation-mauve-grass-",
   ["grass-olive"]="vegetation-olive-grass-",
   ["grass-orange"]="vegetation-orange-grass-",
   ["grass-purple"]="vegetation-purple-grass-",
   ["grass-red"]="vegetation-red-grass-",
   ["grass-turquoise"]="vegetation-turquoise-grass-",
   ["grass-violet"]="vegetation-violet-grass-",
   ["grass-yellow"]="vegetation-yellow-grass-",

   ["sand-aubergine"]="mineral-aubergine-sand-",
   ["sand-beige"]="mineral-beige-sand-",
   ["sand-black"]="mineral-black-sand-",
   ["sand-brown"]="mineral-brown-sand-",
   ["sand-cream"]="mineral-cream-sand-",
   ["sand-dustyrose"]="mineral-dustyrose-sand-",
   ["sand-grey"]="mineral-grey-sand-",
   ["sand-purple"]="mineral-purple-sand-",
   ["sand-red"]="mineral-red-sand-",
   ["sand-tan"]="mineral-tan-sand-",
   ["sand-violet"]="mineral-violet-sand-",
   ["sand-white"]="mineral-white-sand-",

   ["volcanic-blue"]="volcanic-blue-heat-",
   ["volcanic-green"]="volcanic-green-heat-",
   ["volcanic-orange"]="volcanic-orange-heat-",
   ["volcanic-purple"]="volcanic-purple-heat-",
}

function string.starts(String,Start)
   return string.sub(String,1,string.len(Start))==Start
end

for tileName, tile in pairs(data.raw.tile) do

   biome = ""

   for setting, prefix in pairs(biome_settings) do
      if string.starts(tileName,prefix) then
         biome = setting
      end
   end

   log(tileName .. " " .. biome)

   if not (biome == "") then
      for prop, value in pairs(tile) do
         --log("    "..k2)
         if prop == "autoplace" then
            for k3, v3 in pairs(value) do
               if k3 == "probability_expression" then
                  data.raw.tile[tileName].autoplace.probability_expression =
                     (v3 + settings.startup["alien-biomes-settings-offset-" .. biome].value) *
                      settings.startup["alien-biomes-settings-gain-" .. biome].value +
                      settings.startup["alien-biomes-settings-bias-" .. biome].value
               end
            end
         end
      end
   end
end

for k, v in pairs(data.raw["noise-expression"]) do
   log(k)
end
