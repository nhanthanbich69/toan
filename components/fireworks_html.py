import streamlit as st

def fireworks_display():
    html_code = """
    <style>
        body {
            margin: 0;
            overflow: hidden;
            background-color: #ffc0cb; /* nền hồng cute */
        }
        canvas {
            position: fixed;
            top: 0;
            left: 0;
            z-index: 0;
            filter: blur(1px) brightness(1.2); /* glow nhẹ */
        }
        .poem-overlay {
            position: fixed;
            top: 5%;
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            z-index: 10;
            color: #ff0000; /* đỏ rực */
            font-size: 30px;
            font-weight: bold;
            line-height: 1.8;
            text-shadow:
                0 0 5px #ff0033,
                0 0 10px #ff0033,
                0 0 20px #ff3366,
                0 0 30px #ff6699;
        }
        .heart {
            position: fixed;
            width: 20px;
            height: 20px;
            background: url('https://emoji.slack-edge.com/T0GKZLZSE/heart_bounce/795dc5e6e7cdcfaa.gif') no-repeat center center;
            background-size: contain;
            animation: float 6s infinite ease-in-out;
            z-index: 5;
            opacity: 0.8;
        }

        @keyframes float {
            0% {transform: translateY(0) scale(1);}
            50% {transform: translateY(-100px) scale(1.2);}
            100% {transform: translateY(0) scale(1);}
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

    <!-- ❤️ Thêm 20 trái tim bay ngẫu nhiên ❤️ -->
    <script>
        for (let i = 0; i < 20; i++) {
            const heart = document.createElement('div');
            heart.className = 'heart';
            heart.style.left = Math.random() * 100 + 'vw';
            heart.style.top = Math.random() * 100 + 'vh';
            heart.style.animationDelay = (Math.random() * 5) + 's';
            document.body.appendChild(heart);
        }
    </script>

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
            this.hue = Math.random() * 360;
            this.brightness = Math.random() * 50 + 50;
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
            ctx.beginPath();
            ctx.arc(this.x, this.y, 2.5, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${this.hue}, 100%, ${this.brightness}%, ${this.alpha})`;
            ctx.fill();
        }
    }

    function createParticles(x, y) {
        const count = 60;
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
