var adsDebugSas = {
    runDebugAds: false,
    listScript: [],
    enable: false,
    init: function () {

        if (this.runDebugAds) return;

        let style = document.createElement("style");
        style.innerHTML = `
            .debugAdsSas .dimentions {
                font-size: 13px;
                margin: 7px;
            }
            .debugAdsSas {
                position: absolute;
                width: 100%;
                height: 100%;
                background-color: rgba(249, 215, 49, 0.85);
                display: flex;
                align-items: center;
                justify-content: center;
                font-family: monospace;
                flex-direction: column;
                color: #FFF;
                font-size: 85%;
                text-shadow: 2px 3px 2px #000;
                font-weight: 700;
                border-radius: 2px;
                border: 2px dashed #000;
                z-index: 1000;
                animation: 0.5s animateBorderOne ease-out infinite;
            }

            @keyframes animateBorderOne {
                to {
                    border-radius: 5px
                }
            }

            .wrapDebugAdsSas{  
                min-width: 100%;
                min-height: 45px;
                position: relative;
            }
        `;

        let head = document.getElementsByTagName("head")[0];
        head.appendChild(style);

        this.enabled();

        this.runDebugAds = true;
    },
    enabled: function () {
        this.listScript = [].slice.call(document.querySelectorAll("script:not([src]")).filter((script) => {
            if (script.innerHTML.trim().indexOf("sas.cmd.push") == 0 && window.getComputedStyle(script.parentNode).display != 'none') {
                let list_sasCmdPush = script.innerHTML.match(/(\w+)/g);
                script.code = list_sasCmdPush[6];
                script.label = list_sasCmdPush[8];

                var $sas = script.parentNode.querySelectorAll("#sas_" + script.code)[0];
                if (!$sas) return;
                
                $sas.classList.add("wrapDebugAdsSas");
                let debug = this.createDebug(script);
                $sas.insertBefore(debug, $sas.firstElementChild);
                var rects = debug.getClientRects();
                if (rects.length == 0) {
                    console.log('ads oculto de nombre ' + script.label);
                    return;
                }
        
                $sas.debug = debug;
                script.sas = $sas;
        
                debug.setDimentions();

                return true;
            }
        });
        this.enable = true;
    },
    disabled: function () {
        this.listScript.forEach(function (script) {
            script.sas.classList.remove("wrapDebugAdsSas");
            script.sas.debug.remove();
        })
        this.enable = false;
    },
    createDebug: function (script) {
        var div = document.createElement("div");
        var divDimentions = document.createElement("div");
        var divName = document.createElement("div");
        divName.innerHTML = 'SmartAdServer (SAS) - ' + script.code + ' - ' + script.label;

        divDimentions.classList.add("dimentions");

        div.setDimentions = function () {
            let rect = this.getClientRects()[0];
            divDimentions.innerHTML = Math.floor(rect.width) + " X " + Math.floor(rect.height);
        };

        div.classList.add("debugAdsSas");
        div.appendChild(divName);
        div.appendChild(divDimentions);

        return div;
    }
};

adsDebugSas.init();