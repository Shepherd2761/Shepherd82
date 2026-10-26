#!/usr/bin/env python3
"""Generate a curated set of useful ToolNest calculator pages from a data catalog."""
from pathlib import Path
import json, html, re, sys
ROOT=Path(sys.argv[1] if len(sys.argv)>1 else "site")
BASE="https://shepherd2761.github.io/Shepherd82/"
TOOLS=[
  {
    "slug": "percentage-calculator",
    "title": "Percentage Calculator",
    "formula": "percentage",
    "fields": [
      "Value",
      "Percent"
    ],
    "description": "Calculate a percentage of a number."
  },
  {
    "slug": "percentage-increase-calculator",
    "title": "Percentage Increase Calculator",
    "formula": "pctchange",
    "fields": [
      "Original value",
      "New value"
    ],
    "description": "Measure percentage increase between two values."
  },
  {
    "slug": "percentage-decrease-calculator",
    "title": "Percentage Decrease Calculator",
    "formula": "pctchange",
    "fields": [
      "Original value",
      "New value"
    ],
    "description": "Measure percentage decrease between two values."
  },
  {
    "slug": "ratio-calculator",
    "title": "Ratio Calculator",
    "formula": "ratio",
    "fields": [
      "First value",
      "Second value"
    ],
    "description": "Compare two quantities as a ratio and find their shares."
  },
  {
    "slug": "proportion-calculator",
    "title": "Proportion Calculator",
    "formula": "proportion",
    "fields": [
      "A",
      "B",
      "C"
    ],
    "description": "Solve A:B = C:x."
  },
  {
    "slug": "average-speed-calculator",
    "title": "Average Speed Calculator",
    "formula": "speed",
    "fields": [
      "Distance (km)",
      "Time (hours)"
    ],
    "description": "Calculate average travel speed."
  },
  {
    "slug": "distance-calculator",
    "title": "Distance Calculator",
    "formula": "distance",
    "fields": [
      "Speed (km/h)",
      "Time (hours)"
    ],
    "description": "Calculate distance from speed and time."
  },
  {
    "slug": "time-calculator",
    "title": "Travel Time Calculator",
    "formula": "traveltime",
    "fields": [
      "Distance (km)",
      "Speed (km/h)"
    ],
    "description": "Estimate travel time from distance and speed."
  },
  {
    "slug": "rectangle-area-calculator",
    "title": "Rectangle Area Calculator",
    "formula": "rectangle",
    "fields": [
      "Length",
      "Width"
    ],
    "description": "Calculate rectangle area and perimeter."
  },
  {
    "slug": "circle-area-calculator",
    "title": "Circle Area Calculator",
    "formula": "circle",
    "fields": [
      "Radius"
    ],
    "description": "Calculate circle area and circumference."
  },
  {
    "slug": "triangle-area-calculator",
    "title": "Triangle Area Calculator",
    "formula": "triangle",
    "fields": [
      "Base",
      "Height"
    ],
    "description": "Calculate triangle area."
  },
  {
    "slug": "triangle-hypotenuse-calculator",
    "title": "Triangle Hypotenuse Calculator",
    "formula": "hypot",
    "fields": [
      "Side A",
      "Side B"
    ],
    "description": "Calculate a right triangle's hypotenuse."
  },
  {
    "slug": "cylinder-volume-calculator",
    "title": "Cylinder Volume Calculator",
    "formula": "cylinder",
    "fields": [
      "Radius",
      "Height"
    ],
    "description": "Calculate cylinder volume and surface area."
  },
  {
    "slug": "sphere-volume-calculator",
    "title": "Sphere Volume Calculator",
    "formula": "sphere",
    "fields": [
      "Radius"
    ],
    "description": "Calculate sphere volume and surface area."
  },
  {
    "slug": "cube-volume-calculator",
    "title": "Cube Volume Calculator",
    "formula": "cube",
    "fields": [
      "Side length"
    ],
    "description": "Calculate cube volume and surface area."
  },
  {
    "slug": "cone-volume-calculator",
    "title": "Cone Volume Calculator",
    "formula": "cone",
    "fields": [
      "Radius",
      "Height"
    ],
    "description": "Calculate cone volume."
  },
  {
    "slug": "density-calculator",
    "title": "Density Calculator",
    "formula": "density",
    "fields": [
      "Mass",
      "Volume"
    ],
    "description": "Calculate density from mass and volume."
  },
  {
    "slug": "mass-calculator",
    "title": "Mass Calculator",
    "formula": "mass",
    "fields": [
      "Density",
      "Volume"
    ],
    "description": "Calculate mass from density and volume."
  },
  {
    "slug": "volume-calculator",
    "title": "Volume Calculator",
    "formula": "volmass",
    "fields": [
      "Mass",
      "Density"
    ],
    "description": "Calculate volume from mass and density."
  },
  {
    "slug": "mean-calculator",
    "title": "Mean Calculator",
    "formula": "mean",
    "fields": [
      "Comma-separated numbers"
    ],
    "description": "Calculate arithmetic mean."
  },
  {
    "slug": "range-calculator",
    "title": "Range Calculator",
    "formula": "range",
    "fields": [
      "Comma-separated numbers"
    ],
    "description": "Find the range, minimum, and maximum in a dataset."
  },
  {
    "slug": "variance-calculator",
    "title": "Variance Calculator",
    "formula": "variance",
    "fields": [
      "Comma-separated numbers"
    ],
    "description": "Calculate population and sample variance."
  },
  {
    "slug": "standard-deviation-calculator",
    "title": "Standard Deviation Calculator",
    "formula": "stdev",
    "fields": [
      "Comma-separated numbers"
    ],
    "description": "Calculate population and sample standard deviation."
  },
  {
    "slug": "weighted-average-calculator",
    "title": "Weighted Average Calculator",
    "formula": "weighted",
    "fields": [
      "Values (comma-separated)",
      "Weights (comma-separated)"
    ],
    "description": "Calculate a weighted average."
  },
  {
    "slug": "permutation-calculator",
    "title": "Permutation Calculator",
    "formula": "permutation",
    "fields": [
      "n",
      "r"
    ],
    "description": "Calculate the number of ordered selections."
  },
  {
    "slug": "combination-calculator",
    "title": "Combination Calculator",
    "formula": "combination",
    "fields": [
      "n",
      "r"
    ],
    "description": "Calculate the number of unordered selections."
  },
  {
    "slug": "factorial-calculator",
    "title": "Factorial Calculator",
    "formula": "factorial",
    "fields": [
      "Non-negative integer"
    ],
    "description": "Calculate factorial n!."
  },
  {
    "slug": "gcd-calculator",
    "title": "GCD Calculator",
    "formula": "gcd",
    "fields": [
      "Integer A",
      "Integer B"
    ],
    "description": "Find the greatest common divisor."
  },
  {
    "slug": "lcm-calculator",
    "title": "LCM Calculator",
    "formula": "lcm",
    "fields": [
      "Integer A",
      "Integer B"
    ],
    "description": "Find the least common multiple."
  },
  {
    "slug": "prime-checker",
    "title": "Prime Number Checker",
    "formula": "prime",
    "fields": [
      "Integer"
    ],
    "description": "Check whether an integer is prime."
  },
  {
    "slug": "quadratic-formula-calculator",
    "title": "Quadratic Formula Calculator",
    "formula": "quadratic",
    "fields": [
      "a",
      "b",
      "c"
    ],
    "description": "Solve a quadratic equation and report real or complex roots."
  },
  {
    "slug": "slope-intercept-calculator",
    "title": "Slope Calculator",
    "formula": "slope",
    "fields": [
      "x1",
      "y1",
      "x2",
      "y2"
    ],
    "description": "Calculate line slope from two points."
  },
  {
    "slug": "midpoint-calculator",
    "title": "Midpoint Calculator",
    "formula": "midpoint",
    "fields": [
      "x1",
      "y1",
      "x2",
      "y2"
    ],
    "description": "Calculate the midpoint between two coordinate points."
  },
  {
    "slug": "distance-between-points-calculator",
    "title": "Distance Between Points Calculator",
    "formula": "pointdistance",
    "fields": [
      "x1",
      "y1",
      "x2",
      "y2"
    ],
    "description": "Calculate Euclidean distance between two points."
  },
  {
    "slug": "unit-price-calculator",
    "title": "Unit Price Calculator",
    "formula": "unitprice",
    "fields": [
      "Price A",
      "Quantity A",
      "Price B",
      "Quantity B"
    ],
    "description": "Compare unit prices of two packages."
  },
  {
    "slug": "discount-calculator-advanced",
    "title": "Discount Calculator",
    "formula": "discount",
    "fields": [
      "Original price",
      "Discount percent"
    ],
    "description": "Calculate savings and sale price."
  },
  {
    "slug": "sales-tax-calculator-advanced",
    "title": "Sales Tax Calculator",
    "formula": "tax",
    "fields": [
      "Price before tax",
      "Tax rate percent"
    ],
    "description": "Calculate sales tax and total price."
  },
  {
    "slug": "tip-calculator-advanced",
    "title": "Tip Calculator",
    "formula": "tip",
    "fields": [
      "Bill amount",
      "Tip percent",
      "People splitting bill"
    ],
    "description": "Calculate tip, total, and per-person share."
  },
  {
    "slug": "markup-calculator-advanced",
    "title": "Markup Calculator",
    "formula": "markup",
    "fields": [
      "Cost",
      "Markup percent"
    ],
    "description": "Calculate selling price and markup."
  },
  {
    "slug": "profit-margin-calculator-advanced",
    "title": "Profit Margin Calculator",
    "formula": "margin",
    "fields": [
      "Revenue",
      "Cost"
    ],
    "description": "Calculate gross profit and margin percentage."
  },
  {
    "slug": "break-even-calculator",
    "title": "Break-Even Calculator",
    "formula": "breakeven",
    "fields": [
      "Fixed costs",
      "Price per unit",
      "Variable cost per unit"
    ],
    "description": "Calculate break-even units and revenue."
  },
  {
    "slug": "commission-calculator",
    "title": "Commission Calculator",
    "formula": "commission",
    "fields": [
      "Sales amount",
      "Commission percent"
    ],
    "description": "Calculate commission and net after commission."
  },
  {
    "slug": "hourly-to-salary-calculator",
    "title": "Hourly to Salary Calculator",
    "formula": "salary",
    "fields": [
      "Hourly wage",
      "Hours per week",
      "Weeks per year"
    ],
    "description": "Convert hourly pay to annual and monthly gross pay."
  },
  {
    "slug": "overtime-pay-calculator",
    "title": "Overtime Pay Calculator",
    "formula": "overtime",
    "fields": [
      "Hourly rate",
      "Regular hours",
      "Overtime hours",
      "Overtime multiplier"
    ],
    "description": "Estimate gross wages including overtime."
  },
  {
    "slug": "paycheck-calculator-basic",
    "title": "Gross Pay Calculator",
    "formula": "grosspay",
    "fields": [
      "Hourly rate",
      "Hours worked"
    ],
    "description": "Calculate gross pay before deductions."
  },
  {
    "slug": "compound-interest-calculator",
    "title": "Compound Interest Calculator",
    "formula": "compound",
    "fields": [
      "Principal",
      "Annual rate percent",
      "Years",
      "Compounds per year"
    ],
    "description": "Estimate compound growth and interest earned."
  },
  {
    "slug": "simple-interest-calculator",
    "title": "Simple Interest Calculator",
    "formula": "simpleinterest",
    "fields": [
      "Principal",
      "Annual rate percent",
      "Years"
    ],
    "description": "Calculate simple interest and total balance."
  },
  {
    "slug": "cagr-calculator-basic",
    "title": "CAGR Calculator",
    "formula": "cagr",
    "fields": [
      "Starting value",
      "Ending value",
      "Years"
    ],
    "description": "Calculate compound annual growth rate."
  },
  {
    "slug": "inflation-calculator-basic",
    "title": "Inflation Calculator",
    "formula": "inflation",
    "fields": [
      "Current price",
      "Annual inflation percent",
      "Years"
    ],
    "description": "Estimate future price under constant inflation."
  },
  {
    "slug": "savings-goal-calculator",
    "title": "Savings Goal Calculator",
    "formula": "savingsgoal",
    "fields": [
      "Target amount",
      "Current savings",
      "Monthly contribution"
    ],
    "description": "Estimate months needed to reach a savings target."
  },
  {
    "slug": "loan-payment-calculator-basic",
    "title": "Loan Payment Calculator",
    "formula": "loan",
    "fields": [
      "Loan amount",
      "Annual interest percent",
      "Term in years"
    ],
    "description": "Estimate fixed monthly loan payments."
  },
  {
    "slug": "electricity-cost-calculator",
    "title": "Electricity Cost Calculator",
    "formula": "electricity",
    "fields": [
      "Power in watts",
      "Hours per day",
      "Days",
      "Price per kWh"
    ],
    "description": "Estimate energy consumption and electricity cost."
  },
  {
    "slug": "fuel-cost-calculator",
    "title": "Fuel Cost Calculator",
    "formula": "fuel",
    "fields": [
      "Distance (km)",
      "Efficiency (km per liter)",
      "Price per liter"
    ],
    "description": "Estimate fuel required and cost."
  },
  {
    "slug": "ohms-law-calculator",
    "title": "Ohm's Law Calculator",
    "formula": "ohms",
    "fields": [
      "Voltage (V)",
      "Resistance (ohms)"
    ],
    "description": "Calculate current and power using voltage and resistance."
  },
  {
    "slug": "power-calculator",
    "title": "Electrical Power Calculator",
    "formula": "power",
    "fields": [
      "Voltage (V)",
      "Current (A)"
    ],
    "description": "Calculate electrical power."
  },
  {
    "slug": "paint-calculator",
    "title": "Paint Calculator",
    "formula": "paint",
    "fields": [
      "Wall area (sq ft)",
      "Coverage per gallon",
      "Coats"
    ],
    "description": "Estimate paint quantity."
  },
  {
    "slug": "tile-calculator",
    "title": "Tile Calculator",
    "formula": "tile",
    "fields": [
      "Area (sq ft)",
      "Tile area (sq ft)",
      "Waste percent"
    ],
    "description": "Estimate tiles required with waste."
  },
  {
    "slug": "concrete-volume-calculator",
    "title": "Concrete Volume Calculator",
    "formula": "concrete",
    "fields": [
      "Length (ft)",
      "Width (ft)",
      "Depth (inches)"
    ],
    "description": "Estimate concrete volume in cubic feet and yards."
  },
  {
    "slug": "flooring-calculator",
    "title": "Flooring Calculator",
    "formula": "flooring",
    "fields": [
      "Room length (ft)",
      "Room width (ft)",
      "Waste percent"
    ],
    "description": "Estimate flooring area including waste."
  },
  {
    "slug": "gravel-calculator",
    "title": "Gravel Calculator",
    "formula": "gravel",
    "fields": [
      "Length (ft)",
      "Width (ft)",
      "Depth (inches)"
    ],
    "description": "Estimate gravel volume in cubic yards."
  },
  {
    "slug": "mulch-calculator",
    "title": "Mulch Calculator",
    "formula": "mulch",
    "fields": [
      "Area (sq ft)",
      "Depth (inches)"
    ],
    "description": "Estimate mulch volume in cubic yards."
  },
  {
    "slug": "roof-pitch-calculator",
    "title": "Roof Pitch Calculator",
    "formula": "roofpitch",
    "fields": [
      "Rise (inches)",
      "Run (inches)"
    ],
    "description": "Calculate roof pitch, angle, and slope ratio."
  },
  {
    "slug": "stair-calculator",
    "title": "Stair Calculator",
    "formula": "stairs",
    "fields": [
      "Total rise (inches)",
      "Number of risers"
    ],
    "description": "Estimate individual riser height."
  },
  {
    "slug": "bmi-calculator-metric",
    "title": "BMI Calculator (Metric)",
    "formula": "bmi",
    "fields": [
      "Weight (kg)",
      "Height (cm)"
    ],
    "description": "Calculate body mass index from metric measurements."
  },
  {
    "slug": "bmr-calculator-male",
    "title": "BMR Calculator",
    "formula": "bmr",
    "fields": [
      "Weight (kg)",
      "Height (cm)",
      "Age",
      "Sex code (1 male, 0 female)"
    ],
    "description": "Estimate basal metabolic rate using Mifflin-St Jeor."
  },
  {
    "slug": "calorie-deficit-calculator",
    "title": "Calorie Deficit Calculator",
    "formula": "deficit",
    "fields": [
      "Maintenance calories",
      "Daily deficit"
    ],
    "description": "Calculate an illustrative daily calorie target."
  },
  {
    "slug": "protein-intake-calculator",
    "title": "Protein Intake Calculator",
    "formula": "protein",
    "fields": [
      "Body weight (kg)",
      "Grams per kg"
    ],
    "description": "Estimate a daily protein target."
  },
  {
    "slug": "pace-calculator",
    "title": "Running Pace Calculator",
    "formula": "pace",
    "fields": [
      "Distance (km)",
      "Time (minutes)"
    ],
    "description": "Calculate pace per kilometre and mile."
  },
  {
    "slug": "baking-conversion-calculator",
    "title": "Baking Ratio Calculator",
    "formula": "bakingratio",
    "fields": [
      "Ingredient amount",
      "Scale factor"
    ],
    "description": "Scale an ingredient amount for a recipe."
  },
  {
    "slug": "cooking-unit-converter",
    "title": "Cups to Milliliters Converter",
    "formula": "cupsml",
    "fields": [
      "Cups"
    ],
    "description": "Convert US cups to milliliters."
  },
  {
    "slug": "fahrenheit-celsius-converter",
    "title": "Fahrenheit to Celsius Converter",
    "formula": "fahrenheit",
    "fields": [
      "Temperature (°F)"
    ],
    "description": "Convert Fahrenheit to Celsius."
  },
  {
    "slug": "celsius-kelvin-converter",
    "title": "Celsius to Kelvin Converter",
    "formula": "kelvin",
    "fields": [
      "Temperature (°C)"
    ],
    "description": "Convert Celsius to Kelvin."
  },
  {
    "slug": "kilometers-miles-converter",
    "title": "Kilometers to Miles Converter",
    "formula": "kmmi",
    "fields": [
      "Kilometers"
    ],
    "description": "Convert kilometers to miles."
  },
  {
    "slug": "miles-kilometers-converter",
    "title": "Miles to Kilometers Converter",
    "formula": "mikm",
    "fields": [
      "Miles"
    ],
    "description": "Convert miles to kilometers."
  },
  {
    "slug": "kg-lbs-converter",
    "title": "Kilograms to Pounds Converter",
    "formula": "kglb",
    "fields": [
      "Kilograms"
    ],
    "description": "Convert kilograms to pounds."
  },
  {
    "slug": "lbs-kg-converter",
    "title": "Pounds to Kilograms Converter",
    "formula": "lbkg",
    "fields": [
      "Pounds"
    ],
    "description": "Convert pounds to kilograms."
  },
  {
    "slug": "cm-inches-converter",
    "title": "Centimeters to Inches Converter",
    "formula": "cmin",
    "fields": [
      "Centimeters"
    ],
    "description": "Convert centimeters to inches."
  },
  {
    "slug": "inches-cm-converter",
    "title": "Inches to Centimeters Converter",
    "formula": "incm",
    "fields": [
      "Inches"
    ],
    "description": "Convert inches to centimeters."
  },
  {
    "slug": "liters-gallons-converter",
    "title": "Liters to US Gallons Converter",
    "formula": "litgal",
    "fields": [
      "Liters"
    ],
    "description": "Convert liters to US liquid gallons."
  },
  {
    "slug": "gallons-liters-converter",
    "title": "US Gallons to Liters Converter",
    "formula": "gallit",
    "fields": [
      "US gallons"
    ],
    "description": "Convert US liquid gallons to liters."
  },
  {
    "slug": "minutes-hours-converter",
    "title": "Minutes to Hours Converter",
    "formula": "minhr",
    "fields": [
      "Minutes"
    ],
    "description": "Convert minutes to hours and remaining minutes."
  },
  {
    "slug": "hours-minutes-converter",
    "title": "Hours to Minutes Converter",
    "formula": "hrmin",
    "fields": [
      "Hours"
    ],
    "description": "Convert hours to minutes."
  },
  {
    "slug": "days-weeks-converter",
    "title": "Days to Weeks Converter",
    "formula": "dayweek",
    "fields": [
      "Days"
    ],
    "description": "Convert days to weeks and remaining days."
  },
  {
    "slug": "weeks-days-converter",
    "title": "Weeks to Days Converter",
    "formula": "weekday",
    "fields": [
      "Weeks"
    ],
    "description": "Convert weeks to days."
  },
  {
    "slug": "bytes-kilobytes-converter",
    "title": "Bytes to Kilobytes Converter",
    "formula": "byteskb",
    "fields": [
      "Bytes"
    ],
    "description": "Convert bytes to decimal kilobytes and binary kibibytes."
  },
  {
    "slug": "mb-gb-converter",
    "title": "Megabytes to Gigabytes Converter",
    "formula": "mbgb",
    "fields": [
      "Megabytes"
    ],
    "description": "Convert megabytes to decimal gigabytes and binary gibibytes."
  },
  {
    "slug": "word-count-estimator",
    "title": "Word Count Estimator",
    "formula": "wordcount",
    "fields": [
      "Paste text"
    ],
    "description": "Count words, characters, and estimated reading time."
  },
  {
    "slug": "reading-time-estimator",
    "title": "Reading Time Estimator",
    "formula": "readingtime",
    "fields": [
      "Word count",
      "Words per minute"
    ],
    "description": "Estimate reading duration."
  },
  {
    "slug": "loan-to-value-calculator",
    "title": "Loan-to-Value Calculator",
    "formula": "ltv",
    "fields": [
      "Loan amount",
      "Property value"
    ],
    "description": "Calculate loan-to-value ratio."
  },
  {
    "slug": "debt-to-income-calculator",
    "title": "Debt-to-Income Calculator",
    "formula": "dti",
    "fields": [
      "Monthly debt payments",
      "Gross monthly income"
    ],
    "description": "Calculate debt-to-income ratio."
  },
  {
    "slug": "savings-rate-calculator",
    "title": "Savings Rate Calculator",
    "formula": "savingsrate",
    "fields": [
      "Monthly income",
      "Monthly savings"
    ],
    "description": "Calculate personal savings rate."
  },
  {
    "slug": "rental-yield-calculator",
    "title": "Rental Yield Calculator",
    "formula": "rentalyield",
    "fields": [
      "Monthly rent",
      "Property price"
    ],
    "description": "Calculate gross annual rental yield."
  },
  {
    "slug": "inventory-turnover-calculator",
    "title": "Inventory Turnover Calculator",
    "formula": "inventory",
    "fields": [
      "Cost of goods sold",
      "Average inventory"
    ],
    "description": "Calculate inventory turnover ratio."
  },
  {
    "slug": "conversion-rate-calculator",
    "title": "Conversion Rate Calculator",
    "formula": "conversion",
    "fields": [
      "Conversions",
      "Visitors"
    ],
    "description": "Calculate conversion rate."
  },
  {
    "slug": "click-through-rate-calculator",
    "title": "CTR Calculator",
    "formula": "ctr",
    "fields": [
      "Clicks",
      "Impressions"
    ],
    "description": "Calculate click-through rate."
  },
  {
    "slug": "roas-calculator",
    "title": "ROAS Calculator",
    "formula": "roas",
    "fields": [
      "Revenue from ads",
      "Ad spend"
    ],
    "description": "Calculate return on ad spend."
  },
  {
    "slug": "email-open-rate-calculator",
    "title": "Email Open Rate Calculator",
    "formula": "openrate",
    "fields": [
      "Unique opens",
      "Delivered emails"
    ],
    "description": "Calculate email open rate."
  },
  {
    "slug": "churn-rate-calculator",
    "title": "Customer Churn Rate Calculator",
    "formula": "churn",
    "fields": [
      "Customers lost",
      "Customers at start"
    ],
    "description": "Calculate customer churn percentage."
  },
  {
    "slug": "customer-lifetime-value-calculator",
    "title": "Customer Lifetime Value Calculator",
    "formula": "clv",
    "fields": [
      "Average purchase value",
      "Purchases per year",
      "Customer lifespan years"
    ],
    "description": "Estimate simple customer lifetime revenue."
  },
  {
    "slug": "shipping-volumetric-weight-calculator",
    "title": "Volumetric Weight Calculator",
    "formula": "volweight",
    "fields": [
      "Length (cm)",
      "Width (cm)",
      "Height (cm)",
      "Divisor"
    ],
    "description": "Estimate dimensional shipping weight."
  },
  {
    "slug": "data-transfer-time-calculator",
    "title": "Data Transfer Time Calculator",
    "formula": "transfer",
    "fields": [
      "File size (MB)",
      "Speed (Mbps)"
    ],
    "description": "Estimate transfer time for a file."
  },
  {
    "slug": "time-zone-offset-calculator",
    "title": "Minutes-to-Hours Calculator",
    "formula": "minhour",
    "fields": [
      "Minutes"
    ],
    "description": "Convert a minute count to hours and minutes."
  }
]
ENGINE=r"""(()=>{const box=document.querySelector('[data-formula]');if(!box)return;const def=JSON.parse(box.dataset.config),root=document.querySelector('#fields'),out=document.querySelector('#result');def.fields.forEach((label,i)=>{const l=document.createElement('label');l.className='field';l.textContent=label;const input=document.createElement('input');input.id='v'+i;input.type=def.formula==='wordcount'?'text':'number';input.step='any';input.placeholder=def.formula==='wordcount'?'Paste or type text':'Enter '+label.toLowerCase();l.append(input);root.append(l)});const vals=()=>def.fields.map((_,i)=>{const el=document.querySelector('#v'+i);return el.type==='text'?el.value:Number(el.value)});const fmt=x=>Number.isFinite(x)?x.toLocaleString(undefined,{maximumFractionDigits:3}):'—';const money=x=>'$'+fmt(x);function calc(){const v=vals(),a=v[0],b=v[1],c=v[2],d=v[3];let s='';switch(def.formula){
case'percentage':s=fmt(a*b/100)+' is '+fmt(b)+'% of '+fmt(a)+'.';break;
case'pctchange':s='Change: '+fmt(b-a)+'\nPercentage change: '+fmt(a!==0?(b-a)/Math.abs(a)*100:NaN)+'%';break;
case'ratio':{let g=(x,y)=>y?g(y,x%y):Math.abs(x);let z=g(a,b)||1;s='Simplified ratio: '+fmt(a/z)+':'+fmt(b/z)+'\nShare of first: '+fmt((a/(a+b))*100)+'%';break}
case'proportion':s='x = '+fmt(a!==0?b*c/a:NaN);break;
case'speed':s='Average speed: '+fmt(a/b)+' km/h\nAverage speed: '+fmt(a/(b*0.621371))+' mph';break;
case'distance':s='Distance: '+fmt(a*b)+' km';break;case'traveltime':s='Travel time: '+fmt(a/b)+' hours ('+fmt(a/b*60)+' minutes)';break;
case'rectangle':s='Area: '+fmt(a*b)+' square units\nPerimeter: '+fmt(2*(a+b))+' units';break;case'circle':s='Area: '+fmt(Math.PI*a*a)+' square units\nCircumference: '+fmt(2*Math.PI*a)+' units';break;case'triangle':s='Area: '+fmt(a*b/2)+' square units';break;case'hypot':s='Hypotenuse: '+fmt(Math.hypot(a,b));break;
case'cylinder':s='Volume: '+fmt(Math.PI*a*a*b)+' cubic units\nSurface area: '+fmt(2*Math.PI*a*(a+b));break;case'sphere':s='Volume: '+fmt(4*Math.PI*a**3/3)+' cubic units\nSurface area: '+fmt(4*Math.PI*a*a);break;case'cube':s='Volume: '+fmt(a**3)+' cubic units\nSurface area: '+fmt(6*a*a);break;case'cone':s='Volume: '+fmt(Math.PI*a*a*b/3)+' cubic units';break;
case'density':s='Density: '+fmt(a/b)+' mass units per volume unit';break;case'mass':s='Mass: '+fmt(a*b)+' mass units';break;case'volmass':s='Volume: '+fmt(a/b)+' volume units';break;
case'mean':case'range':case'variance':case'stdev':{let ar=String(a).split(',').map(Number).filter(Number.isFinite);if(!ar.length){s='Enter a comma-separated list of numbers.';break}let mean=ar.reduce((x,y)=>x+y,0)/ar.length,pop=ar.reduce((x,y)=>x+(y-mean)**2,0)/ar.length,samp=ar.length>1?pop*ar.length/(ar.length-1):NaN;s=def.formula==='mean'?'Mean: '+fmt(mean):def.formula==='range'?'Minimum: '+fmt(Math.min(...ar))+'\nMaximum: '+fmt(Math.max(...ar))+'\nRange: '+fmt(Math.max(...ar)-Math.min(...ar)):def.formula==='variance'?'Population variance: '+fmt(pop)+'\nSample variance: '+fmt(samp):'Population standard deviation: '+fmt(Math.sqrt(pop))+'\nSample standard deviation: '+fmt(Math.sqrt(samp));break}
case'weighted':{let x=String(a).split(',').map(Number),w=String(b).split(',').map(Number);s=x.length===w.length&&x.length&&w.reduce((p,q)=>p+q,0)!==0?'Weighted average: '+fmt(x.reduce((p,q,i)=>p+q*w[i],0)/w.reduce((p,q)=>p+q,0)):'Values and weights must have the same number of entries and non-zero total weight.';break}
case'permutation':case'combination':{let n=Math.floor(a),r=Math.floor(b),z=1;if(n<0||r<0||r>n||n>170){s='Use integers with 0 ≤ r ≤ n ≤ 170.';break}for(let i=0;i<(def.formula==='combination'?Math.min(r,n-r):r);i++)z*=n-i;if(def.formula==='combination')for(let i=2;i<=r;i++)z/=i;s=(def.formula==='combination'?'Combinations':'Permutations')+': '+fmt(z);break}
case'factorial':{let n=Math.floor(a),z=1;if(n<0||n>170)s='Enter an integer from 0 to 170.';else{for(let i=2;i<=n;i++)z*=i;s=n+'! = '+fmt(z)}break}
case'gcd':case'lcm':{let x=Math.abs(Math.trunc(a)),y=Math.abs(Math.trunc(b)),aa=x,bb=y;while(bb){let t=aa%bb;aa=bb;bb=t}let g=aa;s=def.formula==='gcd'?'GCD: '+g:'LCM: '+(g?Math.abs(x*y)/g:0);break}
case'prime':{let n=Math.floor(a),ok=n>=2;for(let i=2;i<=Math.sqrt(n)&&ok;i++)if(n%i===0)ok=false;s=Number.isInteger(a)?(ok?n+' is prime.':n+' is not prime.'):'Enter an integer.';break}
case'quadratic':{let disc=b*b-4*a*c;s=a===0?(b!==0?'Linear root: '+fmt(-c/b):'a and b cannot both be zero.'):disc>=0?'Discriminant: '+fmt(disc)+'\nRoot 1: '+fmt((-b+Math.sqrt(disc))/(2*a))+'\nRoot 2: '+fmt((-b-Math.sqrt(disc))/(2*a)):'Discriminant: '+fmt(disc)+'\nComplex roots: '+fmt(-b/(2*a))+' ± '+fmt(Math.sqrt(-disc)/(2*Math.abs(a)))+'i';break}
case'slope':case'midpoint':case'pointdistance':{let dx=c-a,dy=d-b;s=def.formula==='slope'?(dx===0?'Vertical line; slope is undefined.':'Slope: '+fmt(dy/dx)+'\nRise: '+fmt(dy)+'\nRun: '+fmt(dx)):def.formula==='midpoint'?'Midpoint: ('+fmt((a+c)/2)+', '+fmt((b+d)/2)+')':'Distance: '+fmt(Math.hypot(dx,dy));break}
case'unitprice':{let x=a/b,y=c/d;s='A unit price: '+money(x)+'\nB unit price: '+money(y)+'\nBetter value: '+(x<y?'Package A':y<x?'Package B':'Same unit price');break}
case'discount':s='Savings: '+money(a*b/100)+'\nSale price: '+money(a*(1-b/100));break;case'tax':s='Tax: '+money(a*b/100)+'\nTotal: '+money(a*(1+b/100));break;case'tip':{let people=c>0?c:1;s='Tip: '+money(a*b/100)+'\nTotal bill: '+money(a*(1+b/100))+'\nPer person: '+money(a*(1+b/100)/people);break}
case'markup':s='Markup amount: '+money(a*b/100)+'\nSelling price: '+money(a*(1+b/100));break;case'margin':s='Gross profit: '+money(a-b)+'\nProfit margin: '+fmt(a!==0?(a-b)/a*100:NaN)+'%';break;
case'breakeven':{let q=a/(b-c);s=b>c?'Break-even units: '+fmt(Math.ceil(q))+'\nBreak-even revenue: '+money(Math.ceil(q)*b):'Price per unit must exceed variable cost.';break}
case'commission':s='Commission: '+money(a*b/100)+'\nAfter commission: '+money(a-a*b/100);break;case'salary':s='Annual gross pay: '+money(a*b*c)+'\nMonthly average: '+money(a*b*c/12)+'\nWeekly gross pay: '+money(a*b);break;case'overtime':{let mult=d>0?d:1.5;s='Regular pay: '+money(a*b)+'\nOvertime pay: '+money(a*c*mult)+'\nTotal gross pay: '+money(a*b+a*c*mult);break}case'grosspay':s='Gross pay: '+money(a*b);break;
case'compound':{let n=d>0?d:1,z=a*Math.pow(1+b/100/n,n*c);s='Future value: '+money(z)+'\nInterest earned: '+money(z-a);break}case'simpleinterest':s='Interest: '+money(a*b/100*c)+'\nTotal amount: '+money(a*(1+b/100*c));break;case'cagr':s=a>0&&b>0&&c>0?'CAGR: '+fmt((Math.pow(b/a,1/c)-1)*100)+'% per year':'Starting value, ending value, and years must be positive.';break;case'inflation':s='Estimated future price: '+money(a*Math.pow(1+b/100,c))+'\nTotal increase: '+money(a*(Math.pow(1+b/100,c)-1));break;
case'savingsgoal':{let gap=a-b;s=gap<=0?'Goal already reached.':'Estimated months: '+fmt(Math.ceil(gap/c))+'\nApproximate years: '+fmt(gap/c/12);break}
case'loan':{let n=c*12,r=b/1200,p=r===0?a/n:a*r/(1-Math.pow(1+r,-n));s='Monthly payment: '+money(p)+'\nTotal paid: '+money(p*n)+'\nTotal interest: '+money(p*n-a);break}
case'electricity':{let k=a/1000*b*c;s='Energy use: '+fmt(k)+' kWh\nEstimated cost: '+money(k*d);break}case'fuel':{let l=a/b;s='Fuel required: '+fmt(l)+' liters\nEstimated cost: '+money(l*c);break}
case'ohms':s='Current: '+fmt(a/b)+' A\nPower: '+fmt(a*a/b)+' W';break;case'power':s='Electrical power: '+fmt(a*b)+' watts';break;
case'paint':s='Paint required: '+fmt(a/b*c)+' gallons (before rounding up)';break;case'tile':s='Tiles including waste: '+fmt(Math.ceil(a/b*(1+c/100)))+' tiles';break;case'concrete':{let ft=a*b*c/12;s='Volume: '+fmt(ft)+' cubic feet\nConcrete: '+fmt(ft/27)+' cubic yards';break}case'flooring':s='Area: '+fmt(a*b)+' sq ft\nWith waste: '+fmt(a*b*(1+c/100))+' sq ft';break;case'gravel':case'mulch':{let depth=def.formula==='gravel'?c/12:b/12,area=def.formula==='gravel'?a*b:a;s='Volume: '+fmt(area*depth/27)+' cubic yards';break}
case'roofpitch':s='Pitch: '+fmt(a/b*12)+':12\nAngle: '+fmt(Math.atan(a/b)*180/Math.PI)+'°\nSlope: '+fmt(Math.hypot(a,b)/b*100)+'%';break;case'stairs':s='Each riser: '+fmt(a/b)+' inches';break;
case'bmi':s='BMI: '+fmt(a/Math.pow(b/100,2))+' kg/m²\nBMI is a screening measure, not a diagnosis.';break;case'bmr':s='Estimated BMR: '+fmt(10*a+6.25*b-5*c+(d===1?5:-161))+' kcal/day\nMifflin-St Jeor estimate; not a medical assessment.';break;case'deficit':s='Illustrative daily target: '+fmt(a-b)+' calories';break;case'protein':s='Daily protein target: '+fmt(a*b)+' grams';break;case'pace':s='Pace: '+fmt(b/a)+' min/km\nPace: '+fmt(b/(a*0.621371))+' min/mile\nSpeed: '+fmt(a/(b/60))+' km/h';break;
case'bakingratio':s='Scaled amount: '+fmt(a*b);break;case'cupsml':s='Milliliters: '+fmt(a*236.588)+' mL';break;case'fahrenheit':s='Celsius: '+fmt((a-32)*5/9)+' °C';break;case'kelvin':s='Kelvin: '+fmt(a+273.15)+' K';break;case'kmmi':s='Miles: '+fmt(a*0.621371)+' mi';break;case'mikm':s='Kilometers: '+fmt(a*1.609344)+' km';break;case'kglb':s='Pounds: '+fmt(a*2.20462262)+' lb';break;case'lbkg':s='Kilograms: '+fmt(a/2.20462262)+' kg';break;case'cmin':s='Inches: '+fmt(a/2.54)+' in';break;case'incm':s='Centimeters: '+fmt(a*2.54)+' cm';break;case'litgal':s='US gallons: '+fmt(a/3.785411784)+' gal';break;case'gallit':s='Liters: '+fmt(a*3.785411784)+' L';break;case'minhr':s=fmt(Math.floor(a/60))+' hours and '+fmt(a%60)+' minutes';break;case'hrmin':s='Minutes: '+fmt(a*60);break;case'dayweek':s=fmt(Math.floor(a/7))+' weeks and '+fmt(a%7)+' days';break;case'weekday':s='Days: '+fmt(a*7);break;case'byteskb':s='Kilobytes (decimal): '+fmt(a/1000)+' kB\nKibibytes (binary): '+fmt(a/1024)+' KiB';break;case'mbgb':s='Gigabytes (decimal): '+fmt(a/1000)+' GB\nGibibytes (binary): '+fmt(a/1024)+' GiB';break;
case'wordcount':{let t=String(a||'').trim(),words=t?t.split(/\s+/).length:0;s='Words: '+words+'\nCharacters: '+String(a||'').length+'\nReading time: '+fmt(words/200)+' minutes at 200 words/minute';break}case'readingtime':s='Estimated reading time: '+fmt(a/b)+' minutes';break;
case'ltv':s='Loan-to-value ratio: '+fmt(a/b*100)+'%';break;case'dti':s='Debt-to-income ratio: '+fmt(a/b*100)+'%';break;case'savingsrate':s='Savings rate: '+fmt(b/a*100)+'%';break;case'rentalyield':s='Gross annual rental yield: '+fmt(a*12/b*100)+'%';break;case'inventory':s='Inventory turnover: '+fmt(a/b)+' times per period';break;case'conversion':case'ctr':case'openrate':case'churn':s='Rate: '+fmt(a/b*100)+'%';break;case'roas':s='ROAS: '+fmt(a/b)+'x\nReturn on ad spend: '+fmt(a/b*100)+'%';break;case'clv':s='Estimated customer lifetime revenue: '+money(a*b*c);break;case'volweight':s='Dimensional weight: '+fmt(a*b*c/(d>0?d:5000))+' kg';break;case'transfer':s='Ideal transfer time: '+fmt(a*8/d)+' seconds (before overhead); Mbps assumed.';break;case'minhour':s=fmt(Math.floor(a/60))+' hours and '+fmt(a%60)+' minutes';break;
default:s='Check the values and try again.'}
out.textContent=s}document.querySelector('#calculate').addEventListener('click',()=>{try{calc()}catch(e){out.textContent='Check your inputs and try again.'}});document.querySelector('#clear').addEventListener('click',()=>{root.querySelectorAll('input').forEach(x=>x.value='');out.textContent='Your result will appear here.'})})();"""
css="""body{font-family:system-ui,-apple-system,Segoe UI,sans-serif;margin:0;color:#172033;background:#f7f9fc;line-height:1.6}header,footer{background:#fff;border-bottom:1px solid #e4e8f0;padding:16px 20px}.container{max-width:900px;margin:auto;padding:0 20px}main{padding-top:28px;padding-bottom:40px}.brand{font-weight:800;color:#172033;text-decoration:none;font-size:22px}.brand span{color:#3867e8}nav{float:right}nav a{margin-left:16px;color:#334155;text-decoration:none}.crumb{font-size:14px;color:#64748b}.panel{background:#fff;border:1px solid #e0e6ef;border-radius:14px;padding:22px;margin:20px 0}.field{display:block;margin:14px 0;font-weight:600}.field input{display:block;box-sizing:border-box;width:100%;padding:12px;margin-top:6px;border:1px solid #cbd5e1;border-radius:8px;font:inherit}.btn{border:0;border-radius:8px;padding:11px 18px;font:inherit;font-weight:700;cursor:pointer;background:#245be8;color:white}.btn.secondary{background:#e8edf7;color:#172033}pre{white-space:pre-wrap;background:#f1f5fb;padding:16px;border-radius:10px;min-height:42px;font:inherit}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:14px}.card{display:block;background:#fff;padding:16px;border:1px solid #e0e6ef;border-radius:12px;color:#172033;text-decoration:none}.card h2{font-size:18px;margin:0 0 6px}.muted{color:#64748b;font-size:14px}"""
for t in TOOLS:
    folder=ROOT/t["slug"];folder.mkdir(parents=True,exist_ok=True)
    title=html.escape(t["title"]);desc=html.escape(t["description"])
    config=html.escape(json.dumps(t,separators=(",",":")))
    fields=""
    page=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} | Free Online Tool | ToolNest</title><meta name="description" content="{desc} Free, browser-based calculator with instant results."><link rel="stylesheet" href="../catalog-tools.css"></head><body><header><div class="container"><a class="brand" href="../">Tool<span>Nest</span></a><nav><a href="../tools/">All Tools</a><a href="../blog/">Blog</a></nav></div></header><main class="container"><p class="crumb"><a href="../tools/">All Tools</a> / {title}</p><h1>{title}</h1><p>{desc} Enter your values below to calculate the result instantly. Runs in your browser without signup.</p><section class="panel" data-formula="{t["formula"]}" data-config="{config}"><div id="fields">{fields}</div><button class="btn" id="calculate" type="button">Calculate</button> <button class="btn secondary" id="clear" type="button">Clear</button><h2>Result</h2><pre id="result" aria-live="polite">Your result will appear here.</pre></section><section class="panel"><h2>How to use this tool</h2><ol><li>Enter each value in the unit shown beside its field.</li><li>Choose Calculate to see the result.</li><li>Check the assumptions and units before using the result for a decision.</li></ol><h2>Formula and assumptions</h2><p>This tool uses a standard mathematical relationship for the stated calculation. Results are estimates where inputs are approximate; check units and source data. Financial, health, construction, and business outputs are informational and do not replace qualified professional advice.</p><h2>Frequently asked questions</h2><h3>Is this calculator free?</h3><p>Yes. It runs in your browser without an account.</p><h3>Are my inputs uploaded?</h3><p>The calculation runs locally in your browser; this page does not send entered values to a calculator server.</p></section><p><a href="../tools/">Browse all ToolNest tools</a></p></main><footer><div class="container">© 2026 ToolNest · Free browser-based utilities</div></footer><script src="../catalog-tools.js"></script></body></html>'''
    (folder/"index.html").write_text(page,encoding="utf-8")
(ROOT/"catalog-tools.js").write_text(ENGINE,encoding="utf-8")
(ROOT/"catalog-tools.css").write_text(css,encoding="utf-8")
# Add generated cards to the existing tools directory without removing earlier links.
idx=ROOT/"tools"/"index.html"
if idx.exists():
    old=idx.read_text(encoding="utf-8")
    cards=''.join(f'<a class="card" href="../{t["slug"]}/"><h2>{html.escape(t["title"])}</h2><p>{html.escape(t["description"])}</p></a>' for t in TOOLS)
    if 'data-catalog-generated="true"' in old:
        old=re.sub(r'<div data-catalog-generated="true">.*?</div>', '<div data-catalog-generated="true">'+cards+'</div>',old,flags=re.S)
    else:
        old=old.replace('</div></main>', '<div data-catalog-generated="true" class="grid">'+cards+'</div></div></main>',1)
    idx.write_text(old,encoding="utf-8")
print(f"Generated {len(TOOLS)} functional calculator pages from catalog.")
