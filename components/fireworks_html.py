import streamlit as st

def fireworks_display():
    html_code = """
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #ffc0cb;
        }
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 0;
            filter: blur(1px) brightness(1.2);
        }

        .poem-overlay {
            position: fixed;
            top: 5%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 10;
            color: white;
            font-size: 30px;
            font-weight: bold;
            line-height: 1.8;
            -webkit-text-stroke: 1px red;
            text-shadow: 2px 2px 4px rgba(255,0,0,0.6);
        }
    </style>

    <canvas id="fireworks"></canvas>

    <div class="poem-overlay">
        Nay sinh nhật bạn Toàn đây,<br>
        Chúc bạn lương lậu mỗi ngày tiến tới.<br>
        Công nợ khớp đúng từng nơi,<br>
        Deadline kịp lúc, thảnh thơi buổi chiều.<br><br>
        Tiền vô chẳng thiếu, chẳng nhầm,<br>
        Hạch toán chính xác, chẳng cần lo chi.<br>
        Tuổi này sống khỏe, sống chill,<br>
        Tình duyên nườm nượp – chẳng lo kiếm tìm.
    </div>

    <script>
    const canvas = document.getElementById('fireworks');
    const ctx = canvas.getContext('2d');
    let w = canvas.width = window.innerWidth;
    let h = canvas.height = window.innerHeight;

    const fireworks = [];
    const particles = [];

    class Firework {
        constructor() {
            this.x = Math.random() * w;
            this.y = h;
            this.tx = Math.random() * w;
            this.ty = Math.random() * h / 2;
            this.distance = this.y - this.ty;
            this.coordinates = [];
            this.angle = Math.atan2(this.ty - this.y, this.tx - this.x);
            this.speed = 3;
            this.acceleration = 1.1;
            this.brightness = Math.random() * 50 + 50;
            for (let i = 0; i < 3; i++) {
                this.coordinates.push([this.x, this.y]);
            }
        }

        update(index) {
            this.coordinates.pop();
            this.coordinates.unshift([this.x, this.y]);
            this.speed *= this.acceleration;
            const vx = Math.cos(this.angle) * this.speed;
            const vy = Math.sin(this.angle) * this.speed;
            this.x += vx;
            this.y += vy;
            if (Math.abs(this.y - this.ty) < 15) {
                createParticles(this.tx, this.ty);
                fireworks.splice(index, 1);
            }
        }

        draw() {
            ctx.beginPath();
            ctx.moveTo(this.coordinates[this.coordinates.length - 1][0], this.coordinates[this.coordinates.length - 1][1]);
            ctx.lineTo(this.x, this.y);
            ctx.strokeStyle = `hsl(${Math.random() * 360}, 100%, ${this.brightness}%)`;
            ctx.lineWidth = 2;
            ctx.stroke();
        }
    }

    class Particle {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            this.angle = Math.random() * 2 * Math.PI;
            this.speed = Math.random() * 12 + 3;
            this.friction = 0.92;
            this.gravity = 1.2;
            this.alpha = 1;
            this.decay = Math.random() * 0.015 + 0.01;
        }

        update(index) {
            this.speed *= this.friction;
            this.x += Math.cos(this.angle) * this.speed;
            this.y += Math.sin(this.angle) * this.speed + this.gravity;
            this.alpha -= this.decay;
            if (this.alpha <= 0) {
                particles.splice(index, 1);
            }
        }

        draw() {
            ctx.save();
            ctx.translate(this.x, this.y);
            ctx.scale(0.3, 0.3);
            ctx.beginPath();
            ctx.moveTo(0, 0);
            ctx.bezierCurveTo(0, -3, -5, -15, -15, -15);
            ctx.bezierCurveTo(-35, -15, -35, 10, -35, 10);
            ctx.bezierCurveTo(-35, 25, -20, 40, 0, 50);
            ctx.bezierCurveTo(20, 40, 35, 25, 35, 10);
            ctx.bezierCurveTo(35, 10, 35, -15, 15, -15);
            ctx.bezierCurveTo(5, -15, 0, -3, 0, 0);
            ctx.closePath();
            ctx.fillStyle = `hsla(0, 100%, 70%, ${this.alpha})`;
            ctx.fill();
            ctx.restore();
        }
    }

    function createParticles(x, y) {
        const count = 40;
        for (let i = 0; i < count; i++) {
            particles.push(new Particle(x, y));
        }
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.globalCompositeOperation = 'destination-out';
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        ctx.fillRect(0, 0, w, h);
        ctx.globalCompositeOperation = 'lighter';

        fireworks.forEach((f, i) => {
            f.update(i);
            f.draw();
        });

        particles.forEach((p, i) => {
            p.update(i);
            p.draw();
        });

        if (Math.random() < 0.08) {
            fireworks.push(new Firework());
        }
    }

    animate();
    </script>
    """

    st.components.v1.html(html_code, height=700)
