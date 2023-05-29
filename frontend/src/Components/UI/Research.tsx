import articleImg from '../../assets/images/article.png';
import caseStudyImg from '../../assets/images/case-study.png';
import researchImg from '../../assets/images/research.png';
import './Research.css';

const researchData=[
    {
        imgURL: researchImg,
        title: 'Research Paper',
        desc: 'To download our research paper. Click here',
        linkURL: '#'
    },
    {
        imgURL: articleImg,
        title: 'Related Articles',
        desc: 'To access all realted articles and research papers. Click here',
        linkURL: '#'
    },
    {
        imgURL: caseStudyImg,
        title: 'Case Study',
        desc: 'To read abour our case study. Click here',
        linkURL: '#'
    },


]

const Research = () => {
  return (
<section>
    <div className='container'>
        <div className="research__top-content">
            <h6 className="subtitle">
                Research
            </h6>
            <h2>Lets have a look at <span className="highlight">our research</span></h2>
            <div className="research__wrapper">
                {
                    researchData.map((item,index)=>(
                        <div className="research__item" key={index}>
                    <h3>{item.title}</h3>
                    <div className="research__img">
                        <img src={item.imgURL} alt="" />
                    </div>
                    <p className="description research_desc">{item.desc}</p>
                    <div>
                        <a href={item.linkURL} className="learn__more">
                            <i className="ri-arrow-right-line"></i>
                        </a>
                    </div>
                </div>
                    ))
                }

            </div>
        </div>

    </div>
</section>
)
}

export default Research