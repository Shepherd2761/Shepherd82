(()=>{const box=document.querySelector('[data-tool]');if(!box)return;const k=box.dataset.tool,O=document.querySelector('#tool-result'),v=id=>Number(document.getElementById(id)?.value||0),n=x=>Number.isFinite(x)?x.toLocaleString(undefined,{maximumFractionDigits:2}):'Check inputs';function calc(){let a=v('a'),b=v('b'),c=v('c'),d=v('d'),e=v('e'),r='';switch(k){
case'concrete':case'footing':case'patio':{let cf=a*b*c/12;r='Volume: '+n(cf/27)+' cubic yards\nCubic feet: '+n(cf)+'\nApprox. 80-lb bags at 0.6 cu ft: '+Math.ceil(cf/.6);break}
case'landscape':{let cf=a*b*c/12;r='Required volume: '+n(cf/27)+' cubic yards\nCubic feet: '+n(cf)+'\nWith 10% extra: '+n(cf/27*1.1)+' cubic yards';break}
case'paint':{let coats=Math.max(1,b),cov=c>0?c:350;r='Estimated paint: '+Math.ceil(a*coats/cov)+' gallons\nCalculated need: '+n(a*coats/cov)+' gallons';break}
case'area':{let area=a*b,w=Math.max(0,c)/100;r='Room area: '+n(area)+' sq ft\nArea with waste: '+n(area*(1+w))+' sq ft\nSquare yards with waste: '+n(area*(1+w)/9);break}
case'pieces':{let area=a*b,ta=c*d/144;r='Area: '+n(area)+' sq ft\nArea with allowance: '+n(area*(1+Math.max(0,e)/100))+' sq ft\nEstimated pieces: '+(ta>0?Math.ceil(area/ta*(1+Math.max(0,e)/100)):0);break}
case'wallpaper':case'drywall':case'mortar':case'stone':{let w=Math.max(0,c)/100,q=b>0?Math.ceil(a*(1+w)/b):0;r='Estimated quantity: '+q+' '+({wallpaper:'rolls',drywall:'sheets',mortar:'bags',stone:'boxes'}[k])+'\nCoverage with allowance: '+n(a*(1+w))+' sq ft';break}
case'roofing':{let ar=a*Math.max(1,b)*(1+Math.max(0,c)/100);r='Roof surface with waste: '+n(ar)+' sq ft\nRoofing squares: '+n(ar/100)+'\nBundles at approx. 33.3 sq ft each: '+Math.ceil(ar/33.3);break}
case'roofpitch':{let s=a/b;r='Pitch: '+n(s*12)+' / 12\nSlope angle: '+n(Math.atan(s)*180/Math.PI)+' degrees\nSlope multiplier: '+n(Math.sqrt(1+s*s));break}
case'decking':{let rows=Math.ceil(b*12/(c+d)),boards=Math.ceil(a/e);r='Board courses: '+rows+'\nBoards per course: '+boards+'\nEstimated boards: '+rows*boards;break}
case'fence':r='Estimated posts: '+(b>0?Math.ceil(a/b)+1:0)+'\nFence length after subtracting gate widths: '+n(Math.max(0,a-c*d))+' ft';break;
case'asphalt':{let cf=a*b*c/12;r='Surface area: '+n(a*b)+' sq ft\nVolume: '+n(cf/27)+' cubic yards\nApprox. material at 1.5 tons/yd³: '+n(cf/27*1.5)+' tons';break}
case'roomarea':r='Area: '+n(a*b)+' sq ft\nPerimeter: '+n(2*(a+b))+' ft\nSquare yards: '+n(a*b/9);break;
case'btu':r='Estimated cooling capacity: '+Math.round(a*(b||20)*(1+c/100)+Math.max(0,d)*600).toLocaleString()+' BTU/hour\nRule-of-thumb estimate only.';break;
case'baseboardheat':r='Estimated heater output: '+n(a*(b||10))+' watts\nApprox. 1,500-watt heater equivalents: '+n(a*(b||10)/1500);break;
case'pool':{let cf=a*b*c;r='Water volume: '+n(cf*7.48052)+' US gallons\nCubic feet: '+n(cf)+'\nCubic meters: '+n(cf*.0283168);break}
case'aquarium':{let g=a*b*c/231;r='Capacity: '+n(g)+' US gallons\nLiters: '+n(g*3.78541);break}
case'watertank':{let g=Math.PI*(a/2)**2*b*7.48052;r='Estimated capacity: '+n(g)+' US gallons\nLiters: '+n(g*3.78541)+'\nAssumes a vertical cylinder.';break}
case'stairs':{let count=Math.max(1,Math.round(a/(b||7.5)));r='Recommended riser count: '+count+'\nApprox. riser height: '+n(a/count)+' inches\nTread count estimate: '+Math.max(0,count-1)+'\nCheck local codes.';break}
case'stringer':{let diag=Math.sqrt(a*a+b*b);r='Stringer slope length: '+n(diag)+' inches ('+n(diag/12)+' ft)\nRiser count estimate: '+Math.ceil(a/(d||7.5))+'\nTread depth: '+n(c)+' inches';break}
case'units':{let ar=a*b,face=c*d/144;r='Wall area: '+n(ar)+' sq ft\nEstimated units: '+(face>0?Math.ceil(ar/face*(1+Math.max(0,e)/100)):0);break}
case'sod':{let ar=a*b*(1+Math.max(0,d)/100);r='Lawn area: '+n(a*b)+' sq ft\nArea with allowance: '+n(ar)+' sq ft\nEstimated rolls: '+(c>0?Math.ceil(ar/c):0);break}
case'grassseed':r='Estimated seed: '+n(a/1000*b*(1+Math.max(0,c)/100))+' lb\nUse seed-label rates for your grass type.';break;
case'fertilizer':r='Fertilizer needed: '+n(a/1000*b)+' lb\nBags needed: '+(c>0?Math.ceil(a/1000*b/c):0)+'\nFollow product label rates.';break;
case'garden':r='Estimated plant positions: '+Math.floor(a*12/c)*Math.floor(b*12/d)+'\nPlants per row: '+Math.floor(a*12/c)+'\nRows: '+Math.floor(b*12/d);break;
case'raisedbed':{let cf=a*b*c/12;r='Soil volume: '+n(cf)+' cubic feet\nCubic yards: '+n(cf/27)+'\nBags needed: '+(d>0?Math.ceil(cf/d):0);break}
case'sprinkler':r='Estimated run time: '+n(a/b*60)+' minutes';break;
case'drip':r='Total flow: '+n(a*b*c)+' gallons/hour\nWater per run: '+n(a*b*c*d)+' gallons';break;
case'countertop':{let ar=a*b/12,q=ar*(1+Math.max(0,d)/100);r='Surface area: '+n(ar)+' sq ft\nArea with allowance: '+n(q)+' sq ft\nEstimated material cost: $'+n(q*c);break}
case'grout':{let ar=a,j=Math.max(0,d),dep=Math.max(0,e),l=Math.max(.1,b),w=Math.max(.1,c),kg=ar*.092903*(j*25.4)*(dep*25.4)*(l+w)/(l*w)*1.6/1000;r='Rough grout estimate: '+n(kg)+' kg\nVerify with product guidance; grout density and joint profile vary.';break}
case'crown':{let lf=2*(a+b);r='Room perimeter: '+n(lf)+' linear ft\nWith allowance: '+n(lf*(1+Math.max(0,c)/100))+' linear ft';break}
case'baseboard':{let lf=Math.max(0,2*(a+b)-c);r='Net baseboard length: '+n(lf)+' linear ft\nWith allowance: '+n(lf*(1+Math.max(0,d)/100))+' linear ft';break}
case'glass':{let ar=a*b*c/144;r='Total glass area: '+n(ar)+' sq ft\nSquare meters: '+n(ar*.092903);break}
case'solarspace':{let count=b>0?Math.floor(a/b):0;r='Estimated panel count: '+count+'\nApprox. system capacity: '+n(count*c/1000)+' kW';break}
case'boxvolume':{let ci=a*b*c,cf=ci/1728;r='Volume: '+n(ci)+' cubic inches\nCubic feet: '+n(cf)+'\nLiters: '+n(cf*28.3168);break}
case'container':{let vol=a*b*c,eff=Math.max(1,Math.min(100,e))/100;r='Container volume: '+n(vol)+' cubic feet\nUsable volume: '+n(vol*eff)+' cubic feet\nEstimated boxes by volume: '+(d>0?Math.floor(vol*eff/d):0)+'\nActual loading depends on dimensions and weight.';break}
case'storage':{let vol=a*b*c,size=vol<200?'5×5 ft (rough guide)':vol<400?'5×10 ft (rough guide)':vol<800?'10×10 ft (rough guide)':vol<1200?'10×15 ft (rough guide)':'10×20 ft or larger (rough guide)';r='Stored volume: '+n(vol)+' cubic feet\nRough unit-size starting point: '+size;break}
case'movingboxes':{let x=Math.max(0,a),y=Math.max(0,b),z=1+Math.max(0,c)/100;r='Small boxes: '+Math.ceil((x*3+y*2)*z)+'\nMedium boxes: '+Math.ceil((x*4+y*3)*z)+'\nLarge boxes: '+Math.ceil((x*2+y)*z)+'\nPlanning estimate only.';break}
default:return}O.textContent=r}document.querySelector('#run-tool')?.addEventListener('click',calc);document.querySelector('#clear-tool')?.addEventListener('click',()=>O.textContent='Your result will appear here.')})();