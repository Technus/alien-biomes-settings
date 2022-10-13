local noise = require("noise")
local tne = noise.to_noise_expression

local tileMetaData=require("tileMetaData")
local util=require("util")

local logMe = true
if __DebugAdapter and logMe then
  data:extend{
    {
      type = "noise-expression",
      name = "target",
      intended_property = "target",
      expression = tne(0)
    }
  }

  local i=1
  for name, tileData in pairs(data.raw.tile) do
    if tileData.autoplace and tileData.autoplace.probability_expression~=nil then
      --require("noiseImpression")(tileData.autoplace.probability_expression);
      data:extend{
        {
          type = "noise-expression",
          name = "settings-target-"..name,
          intended_property = "target",
          expression = util.deepcopy(tileData.autoplace.probability_expression)
        },
      }
      i = i + 1
    end
  end
  
  local halfCount = math.floor((i-1)/2)+1
  local expStep = 2
  local exp = (halfCount/2-1)*expStep
  local current = 1
  local stat="Tile equations:"

  for name, tileData in pairs(data.raw.tile) do
    if tileData.autoplace and tileData.autoplace.probability_expression~=nil then
      local target = noise.var("target")

      local limCloserToNul = math.pow(10,exp-(expStep/2))
      local limCloserToInf = math.pow(10,exp+(expStep/2))
      local expr

      tileData.map_color=util.generateColor(current)

      if current<halfCount then
        if current==1 then--first
          expr = noise.if_else_chain(noise.less_than(target,-limCloserToNul),1e309,-1e309)
          stat=stat.."\n"..(name.." < "..-limCloserToNul).." "..util.RGBtoHEX(tileData.map_color)
        elseif current==halfCount-1 then--last
          expr = noise.if_else_chain(noise.less_than(target,-limCloserToInf),-1e309,noise.less_than(0,target),-1e309,1e309)
          stat=stat.."\n"..(-limCloserToInf.." <= "..name.." <  0").." "..util.RGBtoHEX(tileData.map_color)
        else
          expr = noise.if_else_chain(noise.less_than(target,-limCloserToInf),-1e309,noise.less_than(-limCloserToNul,target),-1e309,1e309)
          stat=stat.."\n"..(-limCloserToInf.." <= "..name.." <  "..-limCloserToNul).." "..util.RGBtoHEX(tileData.map_color)
        end
        exp = exp - expStep
      elseif current>halfCount then
        if current==halfCount+1 then--first
          expr = noise.if_else_chain(noise.less_or_equal(target,0),-1e309,noise.less_or_equal(limCloserToInf,target),-1e309,1e309)
          stat=stat.."\n"..("0 <  "..name.." <= "..limCloserToInf).." "..util.RGBtoHEX(tileData.map_color)
        elseif current==halfCount*2-1 then--last
          expr = noise.if_else_chain(noise.less_or_equal(limCloserToNul,target),1e309,-1e309)
          stat=stat.."\n"..(limCloserToNul.." < "..name).." "..util.RGBtoHEX(tileData.map_color)
        else
          expr = noise.if_else_chain(noise.less_or_equal(target,limCloserToNul),-1e309,noise.less_or_equal(limCloserToInf,target),-1e309,1e309)
          stat=stat.."\n"..(limCloserToNul.." <  "..name.." <= "..limCloserToInf).." "..util.RGBtoHEX(tileData.map_color)
        end
        exp = exp + expStep
      else --position in middle is expr==Zero
        expr = noise.if_else_chain(noise.equals(target,tne(0)),1e309,-1e309)
        stat=stat.."\n"..(name.." == 0").." "..util.RGBtoHEX(tileData.map_color)
      end

      tileData.autoplace.probability_expression = expr
      current = current + 1
    end
  end
  log(stat)
else
  for name, tileData in pairs(data.raw.tile) do
    local biome = ""
    local tileName = name
  
    for unaliased,alias in pairs(tileMetaData.tile_alias) do
      if name == unaliased then
        tileName = alias
        break
      end
    end
  
    for setting, prefix in pairs(tileMetaData.biome_settings) do
      if util.startsWith(tileName, prefix) then
        biome = setting
        break
      end
    end
  
    if tileData.autoplace then
      if tileData.autoplace.probability_expression~=nil then
        if biome ~= "" then
          tileMetaData.biomes_used[biome]=biome
          local expr = tileData.autoplace.probability_expression
          local disabled = noise.var("settings-disabled-"..biome)
          local a = noise.var("settings-a-"..biome)
          local b = noise.var("settings-b-"..biome)
          local c = noise.var("settings-c-"..biome)
  
          tileData.autoplace.probability_expression = noise.if_else_chain(disabled, -1e309, ((expr+a)/b)+c) -- if disabled then -inf else expr end
  
        elseif __DebugAdapter then
          log(tileName.."    No biome")
        end
      elseif __DebugAdapter then
        log(tileName.."    No expression")
      end
    end
  end
  
  for biome, value in pairs(tileMetaData.biomes_used) do
    data:extend{{
      type="autoplace-control",
      name="settings-" .. biome,
      order="zzz-" .. biome .. "-zzz",
      richness=true,
      category="resource"
    }}
    
    data:extend{
      {
        type = "noise-expression",
        name = "settings-disabled-"..biome,
        expression = noise.equals(noise.var("control-setting:settings-" .. biome .. ":size:multiplier"),tne(0))--disable button  size/coverage==0
      },
      {
        type = "noise-expression",
        name = "settings-a-"..biome,
        expression = noise.log2(noise.var("control-setting:settings-" .. biome .. ":frequency:multiplier"))^tne(5) --frequency / scale   0.16 to 6 / 6 to 0.16
      },
      {
        type = "noise-expression",
        name = "settings-b-"..biome,
        expression = noise.var("control-setting:settings-" .. biome .. ":size:multiplier")^tne(3) --size/coverage disable==0 and 0.16 to 6 / 0.16 to 6
      },
      {
        type = "noise-expression",
        name = "settings-c-"..biome,
        expression = (noise.log2(noise.var("control-setting:settings-" .. biome .. ":richness:multiplier"))^tne(9))*tne(60) --richness 0.16 to 6
      },
    }
  
    if __DebugAdapter then
      data:extend{{
        type = "noise-expression",
        name = "compile-log-test-size-".. biome,
        intended_property = "size",
        expression = noise.compile_time_log(
            noise.to_noise_expression("control-setting:settings-" .. biome .. ":size:multiplier"),
            noise.var("control-setting:settings-" .. biome .. ":size:multiplier")
        )
      }}
      data:extend{{
        type = "noise-expression",
        name = "compile-log-test-frequency-".. biome,
        intended_property = "frequency",
        expression = noise.compile_time_log(
            noise.to_noise_expression("control-setting:settings-" .. biome .. ":frequency:multiplier"),
            noise.var("control-setting:settings-" .. biome .. ":frequency:multiplier")
        )
      }}
      data:extend{{
        type = "noise-expression",
        name = "compile-log-test-richness-".. biome,
        intended_property = "richness",
        expression = noise.compile_time_log(
            noise.to_noise_expression("control-setting:settings-" .. biome .. ":richness:multiplier"),
            noise.var("control-setting:settings-" .. biome .. ":richness:multiplier")
        )
      }}
    end
  end
end