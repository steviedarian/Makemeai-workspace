//+------------------------------------------------------------------+
//| MakeMeAI Swing Trader EA                                         |
//| Stage 1: Daily Trend Detection (Swing Structure)                 |
//| Strategy: Olusegun Dare — MakeMeAI Consulting Ltd               |
//+------------------------------------------------------------------+
#property copyright "MakeMeAI Consulting Ltd"
#property version   "1.00"
#property strict

//--- Input Parameters
input int  SwingLookback  = 5;     // Candles each side to confirm a swing point
input int  SwingHistory   = 100;   // How many daily candles to look back through
input bool ShowTrendInfo  = true;  // Display trend label on chart

//--- Trend States
enum TREND_STATE
{
   TREND_UP,       // Higher Highs + Higher Lows
   TREND_DOWN,     // Lower Highs + Lower Lows
   TREND_RANGING   // Mixed — no clear structure
};


//+------------------------------------------------------------------+
//| Returns true if the candle at [bar] is a swing high              |
//| A swing high has a higher high than the N candles on each side   |
//+------------------------------------------------------------------+
bool IsSwingHigh(string symbol, int bar, int lookback)
{
   double pivotHigh = iHigh(symbol, PERIOD_D1, bar);

   for(int i = 1; i <= lookback; i++)
   {
      // Check left side
      if(bar + i >= iBars(symbol, PERIOD_D1)) return false;
      if(iHigh(symbol, PERIOD_D1, bar + i) >= pivotHigh) return false;

      // Check right side (more recent candles, lower index numbers)
      if(bar - i < 0) return false;
      if(iHigh(symbol, PERIOD_D1, bar - i) >= pivotHigh) return false;
   }
   return true;
}


//+------------------------------------------------------------------+
//| Returns true if the candle at [bar] is a swing low               |
//| A swing low has a lower low than the N candles on each side      |
//+------------------------------------------------------------------+
bool IsSwingLow(string symbol, int bar, int lookback)
{
   double pivotLow = iLow(symbol, PERIOD_D1, bar);

   for(int i = 1; i <= lookback; i++)
   {
      if(bar + i >= iBars(symbol, PERIOD_D1)) return false;
      if(iLow(symbol, PERIOD_D1, bar + i) <= pivotLow) return false;

      if(bar - i < 0) return false;
      if(iLow(symbol, PERIOD_D1, bar - i) <= pivotLow) return false;
   }
   return true;
}


//+------------------------------------------------------------------+
//| Collects the most recent swing highs into an array               |
//| Returns how many were found                                       |
//+------------------------------------------------------------------+
int GetRecentSwingHighs(string symbol, double &highs[], int maxCount)
{
   ArrayResize(highs, maxCount);
   int found = 0;

   // Start after the lookback buffer so right-side candles exist
   for(int bar = SwingLookback + 1; bar < SwingHistory && found < maxCount; bar++)
   {
      if(IsSwingHigh(symbol, bar, SwingLookback))
      {
         highs[found] = iHigh(symbol, PERIOD_D1, bar);
         found++;
      }
   }
   return found;
}


//+------------------------------------------------------------------+
//| Collects the most recent swing lows into an array                |
//| Returns how many were found                                       |
//+------------------------------------------------------------------+
int GetRecentSwingLows(string symbol, double &lows[], int maxCount)
{
   ArrayResize(lows, maxCount);
   int found = 0;

   for(int bar = SwingLookback + 1; bar < SwingHistory && found < maxCount; bar++)
   {
      if(IsSwingLow(symbol, bar, SwingLookback))
      {
         lows[found] = iLow(symbol, PERIOD_D1, bar);
         found++;
      }
   }
   return found;
}


//+------------------------------------------------------------------+
//| Determines the daily trend for a given symbol                    |
//| Logic: compare the two most recent swing highs and swing lows    |
//+------------------------------------------------------------------+
TREND_STATE GetDailyTrend(string symbol)
{
   double swingHighs[], swingLows[];

   int numHighs = GetRecentSwingHighs(symbol, swingHighs, 3);
   int numLows  = GetRecentSwingLows(symbol, swingLows, 3);

   // Need at least 2 of each to compare
   if(numHighs < 2 || numLows < 2)
      return TREND_RANGING;

   // swingHighs[0] = most recent swing high
   // swingHighs[1] = the one before it
   bool higherHighs = swingHighs[0] > swingHighs[1];
   bool higherLows  = swingLows[0]  > swingLows[1];
   bool lowerHighs  = swingHighs[0] < swingHighs[1];
   bool lowerLows   = swingLows[0]  < swingLows[1];

   if(higherHighs && higherLows) return TREND_UP;
   if(lowerHighs  && lowerLows)  return TREND_DOWN;

   return TREND_RANGING;
}


//+------------------------------------------------------------------+
//| EA Initialization                                                 |
//+------------------------------------------------------------------+
int OnInit()
{
   Print("=== MakeMeAI Swing Trader EA — Stage 1 Loaded ===");
   Print("Symbol: ", _Symbol);
   Print("Swing lookback: ", SwingLookback, " candles each side");
   return INIT_SUCCEEDED;
}


//+------------------------------------------------------------------+
//| Main tick function — runs on every price tick                    |
//+------------------------------------------------------------------+
void OnTick()
{
   // Only re-evaluate when a new daily candle opens
   // Avoids running this heavy logic on every tick
   static datetime lastCheckedBar = 0;
   datetime currentDailyBar = iTime(_Symbol, PERIOD_D1, 0);

   if(currentDailyBar == lastCheckedBar) return;
   lastCheckedBar = currentDailyBar;

   // --- Evaluate Daily Trend ---
   TREND_STATE trend = GetDailyTrend(_Symbol);

   string trendLabel;
   color  labelColor;

   switch(trend)
   {
      case TREND_UP:
         trendLabel = "UPTREND — Looking for BUYS";
         labelColor = clrLime;
         break;
      case TREND_DOWN:
         trendLabel = "DOWNTREND — Looking for SELLS";
         labelColor = clrRed;
         break;
      default:
         trendLabel = "RANGING — No trades, waiting for structure";
         labelColor = clrGray;
         break;
   }

   Print(_Symbol, " | Daily Trend: ", trendLabel);

   if(ShowTrendInfo)
      Comment("\nMakeMeAI Swing Trader\n",
              "Symbol : ", _Symbol, "\n",
              "Trend  : ", trendLabel, "\n",
              "Time   : ", TimeToString(TimeCurrent(), TIME_DATE|TIME_MINUTES));
}


//+------------------------------------------------------------------+
//| EA Shutdown                                                       |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   Comment("");
   Print("MakeMeAI Swing Trader EA — Stopped");
}
//+------------------------------------------------------------------+
