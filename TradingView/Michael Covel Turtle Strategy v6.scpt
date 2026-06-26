//@version=6
strategy("Michael Covel Turtle Strategy (Chandelier Exit) v6", overlay=true, initial_capital=10000, default_qty_type=strategy.cash, default_qty_value=1000, pyramiding=50)

// --- Inputs ---
donchianLength  = input.int(55, title="Donchian Channel Length")
atrLength       = input.int(22, title="Chandelier ATR Length")
atrMultiplier   = input.float(5, title="Chandelier ATR Multiplier")
addAmountCash   = input.float(1000.0, title="Cash Amount to Add per Breakout ($)")

// --- Indicators ---
// 55-day Donchian Channel Upper Bound (calculated from previous bars to avoid looking ahead)
upperDonchian = ta.highest(high[1], donchianLength)

// Chandelier Exit Component Calculations
atrValue = ta.atr(atrLength)
highestHigh22 = ta.highest(high, atrLength)

// Calculate the trailing Chandelier Exit stop level
var float chandelierStop = na

if strategy.position_size > 0
    // The stop can only move up, hanging 4.7 ATR below the 22-day highest high
    float currentStop = highestHigh22 - (atrValue * atrMultiplier)
    chandelierStop := na(chandelierStop[1]) ? currentStop : math.max(currentStop, chandelierStop[1])
else
    chandelierStop := na

// --- Position Tracking & Pyramiding Logic ---
// Track bars to ensure we only enter/scale once per day
var int lastTradeBarIndex = -1

// Rule 1: Buy breakout of the 55-day upper bound
bool buySignal = ta.crossover(close, upperDonchian)

// Rule 3: Add $1000 worth of shares, limited to once per day
if buySignal and bar_index != lastTradeBarIndex
    // Calculate quantity based on the dollar amount ($1000) divided by current price
    float qtyToAdd = addAmountCash / close
    strategy.entry("Turtle Long", strategy.long, qty=qtyToAdd)
    lastTradeBarIndex := bar_index

// Rule 2: Sell when the close drops below the Chandelier Exit level
if strategy.position_size > 0 and close < chandelierStop
    strategy.close("Turtle Long", comment="Chandelier Exit")

// --- Plots ---
plot(upperDonchian, color=color.green, title="55d Donchian Upper Bound", linewidth=2)
plot(strategy.position_size > 0 ? chandelierStop : na, color=color.red, title="Chandelier Exit Stop", style=plot.style_linebr, linewidth=2)
