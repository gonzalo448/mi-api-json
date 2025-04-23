
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
<link rel="stylesheet" href="https://site-assets.fontawesome.com/releases/v6.6.0/css/all.css">
<link rel="stylesheet" href="https://site-assets.fontawesome.com/releases/v6.6.0/css/sharp-duotone-solid.css">

<style>
    body {
        background-color: #0f0f1a;
        font-family: 'Inter';
    }

    #current-title {
        font-family: 'Questrial';
        /* Cambiar a Gusto */
    }

    #current-artist {
        font-family: monospace;
        /* Cambiar a Gusto */
        font-weight: 100;
        opacity: 0.5;
    }

    .bg-blur {
        border-radius: 16px;
        box-shadow: 10px 10px 30px #0a0a12, -10px -10px 30px #141422;
        backdrop-filter: blur(12.6px);
        -webkit-backdrop-filter: blur(12.6px);
        border: 1px solid rgba(36, 32, 117, 1);
    }

    .boton {
        width: 40px;
        height: 40px;
        background: #ececec80;
        color: rgb(0, 38, 72);
        border: none;
        border-radius: 50%;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 20pt;
        transition: 0.1s ease-in-out;
    }

    .boton:hover {
        transform: scale(1.15);
        opacity: 0.7;
    }

    #caratula {
        width: 100%;
        max-width: 150px;
        height: auto;
        border-radius: 12px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.6);
    }

    .redes {
        padding: 0;
        display: flex;
        align-items: center;
        gap: 10px;
        list-style: none;
        font-size: 10pt;
    }

    @media screen and (max-width: 560px) {
        .redes {
            margin-top: -8px;
        }

        #logo,
        #nombre {
            display: none;
        }
    }

    .redes li a {
        color: #7de0c6;
        text-decoration: none;
    }

    #visualizer-container {
        position: absolute;
        display: flex;
        justify-content: space-around;
        align-items: flex-end;
        padding: 20px;
        overflow: hidden;
        gap: 3px;
        bottom: -10px;
        margin-left: -20px;
    }

    .bar {
        width: 5px;
        background: linear-gradient(to top, #4a00e0, #8e2de2);
        border-radius: 10px 10px 0 0;
        transition: height 0.1s ease;
        position: relative;
        overflow: hidden;

    }

    .bar::after {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 10px;
        background: rgba(255, 255, 255, 0.3);
        border-radius: 50%;
        filter: blur(5px);
    }
</style>

 <div class="w-100 p-2 bg-blur d-flex gap-3 align-items-center position-relative">
    <div>
        <img src="" id="caratula">
    </div>
    <div class="d-flex flex-column">
        <h4 id="current-title"></h4>
        <h6 style="margin-top: -10px;"><small id="current-artist"></small></h6>
        <div class="d-flex align-items-center gap-4">
            <ul class="redes">
                <!-- Cambiar las Url de cada Red -->
                <li><a href=""><i class="fa-brands fa-facebook-f"></i></a></li>
                <li><a href=""><i class="fa-brands fa-instagram"></i></a></li>
                <li><a href=""><i class="fa-brands fa-x-twitter"></i></a></li>
                <li><a href=""><i class="fa-brands fa-telegram"></i></a></li>
                <li><a href=""><i class="fa-brands fa-tiktok"></i></a></li>
                <li><a href=""><i class="fa-brands fa-youtube"></i></a></li>
                <li><a href=""><i class="fa-brands fa-whatsapp"></i></a></li>
            </ul>
        </div>
        <div class="position-absolute" style="bottom: 10px; right: 10px;">
            <button class="boton" id="player"><i
                    class="fa-sharp-duotone fa-solid fa-circle-play"></i></button>
        </div>
        <div class="position-absolute d-flex gap-2 align-items-center" style="top: 10px; right: 10px;">
            <img src="" width="20" id="logo" style="margin-top: -8px;">
            <h6><small id="nombre" style="font-family: 'Questrial';"></small></h6>
        </div>

        <div id="visualizer-container">
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
            <div class="bar"></div>
        </div>
    </div>
</div>

<script>
    let info = {
        nombre: '', //nombre de la radio
        background: 'linear-gradient(145deg, #181830, #14142c)', // cambio de color de fondo
        texto: '#e0e1dd', // cambio de color de texto
        api: 'http://localhost:2035/status-json.xsl', //no modificar
        streaming: 'https://mox.moxapps.shop/stream', //no modificar        
        RadiobossInfo: 'https://ritmoboss.moxapps.shop/?pass=moxradioserver&action=playbackinfo', //no modificar    
        RadiobossImg: 'https://ritmoboss.moxapps.shop/?pass=moxradioserver&action=trackartwork', //no modificar 
        logo: '' //Url del Logo
    }

    let card = document.querySelectorAll('.bg-blur')
    card.forEach(element => {
        element.style.background = info.background
        element.style.color = info.texto
    })

    document.getElementById('nombre').innerText = info.nombre
    document.getElementById('logo').src = info.logo


    /* Control de Metadata */

    function fetchPlaybackInfo() {
        fetch(info.RadiobossInfo)
            .then(response => response.text())
            .then(str => new window.DOMParser().parseFromString(str, "text/xml"))
            .then(data => {
                const currentTrack = data.querySelector('CurrentTrack TRACK');
                const prevTrack = data.querySelector('PrevTrack TRACK');
                const nextTrack = data.querySelector('NextTrack TRACK');

                document.getElementById('current-artist').textContent = currentTrack.getAttribute('ARTIST');
                document.getElementById('current-title').textContent = currentTrack.getAttribute('TITLE');

                /* const randomParam = Date.now(); */
                const imageUrl = 'https://ritmoboss.moxapps.shop/?pass=moxradioserver&action=trackartwork&random=Date.now()';

                const img = new Image();
                img.onload = function () {
                    document.getElementById('caratula').src = this.src;
                };
                img.src = imageUrl;                
            })
            .catch(console.error);

    }

    fetchPlaybackInfo();
    setInterval(fetchPlaybackInfo, 5000);

    /* Control de Audio */

    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    const analyser = audioContext.createAnalyser();
    const streamUrl = info.streaming;
    let audio = new Audio(streamUrl);
    let source;

    const visualizer = document.getElementById('visualizer-container');
    const player = document.getElementById('player');
    const bars = document.getElementsByClassName('bar');

    audio.crossOrigin = "anonymous";

    audio.addEventListener('playing', function () {
        player.innerHTML = '<i class="fa-sharp-duotone fa-solid fa-circle-stop"></i>';
    });

    audio.addEventListener('waiting', function () {
        player.innerHTML = '<i class="fa-duotone fa-solid fa-spinner-third fa-spin"></i>';
    });

    function playAudio() {
        if (audioContext.state === 'suspended') {
            audioContext.resume();
        }

        if (audio.paused) {            
            if (!source) {
                source = audioContext.createMediaElementSource(audio);
                source.connect(analyser);
                analyser.connect(audioContext.destination);
            }
            audio.src = streamUrl
            audio.play();
            player.innerHTML = '<i class="fa-sharp-duotone fa-solid fa-circle-stop"></i>';
        } else {            
            audio.src = '';            
            player.innerHTML = '<i class="fa-sharp-duotone fa-solid fa-circle-play"></i>';
        }
        visualize();
    }

    function visualize() {
        analyser.fftSize = 64;
        const bufferLength = analyser.frequencyBinCount;
        const dataArray = new Uint8Array(bufferLength);

        function animate() {
            requestAnimationFrame(animate);
            analyser.getByteFrequencyData(dataArray);

            for (let i = 0; i < bars.length; i++) {
                const barHeight = Math.min(dataArray[i] / 8, 500);
                bars[i].style.height = barHeight + 'px';
            }
        }

        animate();
    }

    player.addEventListener('click', playAudio);

</script>
