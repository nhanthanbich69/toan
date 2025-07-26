document.addEventListener("DOMContentLoaded", function() {
    const canvas = document.getElementById("canvas");
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    const ctx = canvas.getContext("2d");

    function draw() {
        ctx.fillStyle = "rgba(0,0,0,0.1)";
        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < 100; i++) {
            ctx.beginPath();
            ctx.arc(Math.random() * canvas.width, Math.random() * canvas.height,
                    Math.random() * 3 + 1, 0, Math.PI * 2);
            ctx.fillStyle = `hsl(${Math.random() * 360}, 100%, 50%)`;
            ctx.fill();
        }
        requestAnimationFrame(draw);
    }
    draw();
});