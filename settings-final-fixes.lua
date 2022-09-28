local allowed_values = function() return {"Enabled", "Disabled"} end

local biome_settings = {
  "dirt-aubergine",
  "dirt-beige",
  "dirt-black",
  "dirt-brown",
  "dirt-cream",
  "dirt-dustyrose",
  "dirt-grey",
  "dirt-purple",
  "dirt-red",
  "dirt-tan",
  "dirt-violet",
  "dirt-white",
  "frozen",
  "grass-blue",
  "grass-green",
  "grass-mauve",
  "grass-olive",
  "grass-orange",
  "grass-purple",
  "grass-red",
  "grass-turquoise",
  "grass-violet",
  "grass-yellow",
  "sand-aubergine",
  "sand-beige",
  "sand-black",
  "sand-brown",
  "sand-cream",
  "sand-dustyrose",
  "sand-grey",
  "sand-purple",
  "sand-red",
  "sand-tan",
  "sand-violet",
  "sand-white",
  "volcanic-blue",
  "volcanic-green",
  "volcanic-orange",
  "volcanic-purple",
}

for _, setting in pairs(biome_settings) do
  data:extend({{
      type = "string-setting",
      name = "alien-biomes-settings-spacer-"..setting,--post
      setting_type = "startup",
      default_value = setting,
      allowed_values = {setting},
      order = "a-" .. setting .. "-a"
  }})
  data:extend({{
      type = "double-setting",
      name = "alien-biomes-settings-offset-"..setting,--pre
      setting_type = "startup",
      default_value = 0,
      order = "a-" .. setting.. "-b"
  }})
  data:extend({{
      type = "double-setting",
      name = "alien-biomes-settings-gain-"..setting,--middle
      setting_type = "startup",
      default_value = 1,
      order = "a-" .. setting.. "-c"
  }})
  data:extend({{
      type = "double-setting",
      name = "alien-biomes-settings-bias-"..setting,--post
      setting_type = "startup",
      default_value = 0,
      order = "a-" .. setting.. "-d"
  }})
end
