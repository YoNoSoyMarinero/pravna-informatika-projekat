import Carousel from 'react-bootstrap/Carousel';
import backgroundImage from '../assets/background.png';
import caseSvg from '../assets/case.svg';
import docsSvg from '../assets/docs.svg';
import lawSvg from '../assets/law.svg';

export const LandingPage = () => {
    return (
        <Carousel>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={backgroundImage}
                    alt="First slide"
                />
                <img
                style={{ position: 'absolute', top: 0, left: 0 }}
                src={docsSvg}
                alt="Overlay"
                />
                <Carousel.Caption>
                    <h3>Прибављање правних докумената:</h3>
                    <p>Корисници могу добити пресуде и законе који су сачувани у AkomaNtoso формату пружањем имена документа.
                       Ова функционалност омогућава корисницима да брзо и ефикасно приступе потребним правним документима за њихове потребе, што олакшава истраживање и рад.</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={backgroundImage}
                    alt="Second slide"
                />
                <img
                style={{ position: 'absolute', top: 0, left: 0 }}
                src={lawSvg}
                alt="Overlay"
                />
                <Carousel.Caption>
                    <h3>Одлучивање засновано на правилима</h3>
                    <p>Користећи DR-Device и RuleML за одлучивање засновано на правилима, систем помаже у правним одлукама користећи постављена правила и логичке претпоставке.
                       Ова технологија обезбеђује анализу правних питања и доношење одговарајућих закључака на основу постављених правила и чињеница.</p>
                </Carousel.Caption>
            </Carousel.Item>
            <Carousel.Item>
                <img
                    className="d-block w-100"
                    src={backgroundImage}
                    alt="Third slide"
                />
                <img
                style={{ position: 'absolute', top: 0, left: 0 }}
                src={caseSvg}
                alt="Overlay"
                />
                <Carousel.Caption>
                    <h3>Одлучивање засновано на случају</h3>
                    <p> Употребом ANNOY за претрагу помоћу векторске сличности, систем проналази сличне случајеве на основу датих чињеница из базе случајева.
                        Ова функција олакшава правним стручњацима да пронађу релевантне примере и претходне случајеве који могу бити корисни за анализу нових случајева и доношење одлука.</p>
                </Carousel.Caption>
            </Carousel.Item>
        </Carousel>
    );
}

export default LandingPage;
