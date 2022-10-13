local doingAnalysis = false

if __DebugAdapter and doingAnalysis then
  require("noiseAnalysis")()
else
  require("noiseSettings")()
end