import {
    Brain,
    Database,
    Code2,
    Target,
    Award,
    User,
    Rocket,
    Cpu
} from "lucide-react";

function About() {

    return (

        <div className="about-page">

            <section className="about-hero">

                <h1>Career Compass AI</h1>

                <p>
                    AI Powered Career Recommendation System that helps students
                    discover the most suitable career path using Machine Learning.
                </p>

            </section>

            <section className="about-grid">

                <div className="about-card">

                    <Target size={40} />

                    <h2>Our Mission</h2>

                    <p>
                        Help students choose the right career by analyzing
                        academic performance and technical skills.
                    </p>

                </div>

                <div className="about-card">

                    <Brain size={40} />

                    <h2>Machine Learning</h2>

                    <p>
                        Predicts the most suitable career with nearly
                        97% accuracy.
                    </p>

                </div>

                <div className="about-card">

                    <Database size={40} />

                    <h2>Database</h2>

                    <p>
                        Stores every prediction securely using MySQL.
                    </p>

                </div>

            </section>

            <section>

                <h2 className="section-title">
                    Technology Stack
                </h2>

                <div className="tech-grid">

                    <div className="tech-card"><Code2 size={28}/> Python</div>
                    <div className="tech-card"><Rocket size={28}/> FastAPI</div>
                    <div className="tech-card"><Cpu size={28}/> React</div>
                    <div className="tech-card"><Database size={28}/> MySQL</div>
                    <div className="tech-card"><Brain size={28}/> Scikit Learn</div>
                    <div className="tech-card"><Award size={28}/> Pandas</div>

                </div>

            </section>

            <section className="developer-card">

                <User size={55}/>

                <h2>Developed By</h2>

                <h3>Suraj Kumar Tiwari</h3>

                <p>
                    B.Tech CSE Student | Machine Learning Enthusiast |
                    Full Stack Developer
                </p>

            </section>

        </div>

    );
}

export default About;