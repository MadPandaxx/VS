import { Carousel } from "react-bootstrap";
import foto3 from './../Asset/foto3.jpg'
import foto1 from './../Asset/foto1.jpg'
import foto9 from './../Asset/foto9.jpg'
import foto6 from './../Asset/foto6.jpg'

const Hero = ()=> {
    return (
        <Carousel>
                <Carousel.Item>
                <img 
                  className="d-block w-100"
                  src={foto3}
                  alt="First Slide"
                  />
                  <Carousel.Caption>
                    <h3>Di Circle K</h3>
                    <p>Si Malu bertemu dengan Si Cegil.</p>
                  </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                <img 
                  className="d-block w-100"
                  src={foto1}
                  alt="In Hoja (Favorite Cafe)"
                  />
                  <Carousel.Caption>
                    <h3>In Hoja (Favorite Cafe)</h3>
                    <p>Tempat Kopi yang sering kita kunjungi kalo bingung mau kemana.</p>
                  </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                <img 
                  className="d-block w-100"
                  src={foto9}
                  alt="Pantai Nich"
                  />
                  <Carousel.Caption>
                    <h3>Healing Di Pantai</h3>
                    <p>Parangtritis Beach</p>
                  </Carousel.Caption>
                </Carousel.Item>
                <Carousel.Item>
                <img
                  className="d-block w-100"
                  src={foto6}
                  alt="CGV"
                  />
                  <Carousel.Caption>
                    <h4>CGV</h4>
                    <p>Nunggu 1 jam setengah untuk nonton Inside Out 2</p>
                  </Carousel.Caption>              
                </Carousel.Item>
        </Carousel>
    );
}
          
export default Hero;