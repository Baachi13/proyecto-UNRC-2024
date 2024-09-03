import React from 'react';

const galleryImages = [
  'assets/img/gallery/gallery-1.jpg',
  'assets/img/gallery/gallery-2.jpg',
  'assets/img/gallery/gallery-3.jpg',
  'assets/img/gallery/gallery-4.jpg',
  'assets/img/gallery/gallery-5.jpg',
  'assets/img/gallery/gallery-6.jpg',
  'assets/img/gallery/gallery-7.jpg',
  'assets/img/gallery/gallery-8.jpg'
];

const Gallery = () => {
  return (
    <section id="gallery" className="gallery section">
      <div className="container section-title" data-aos="fade-up">
        <h2>Gallery</h2>
        <p>Necessitatibus eius consequatur ex aliquid fuga eum quidem sint consectetur velit</p>
      </div>
      <div className="container-fluid" data-aos="fade-up" data-aos-delay="100">
        <div className="row g-0">
          {galleryImages.map((image, index) => (
            <div className="col-lg-3 col-md-4" key={index}>
              <div className="gallery-item">
                <a href={image} className="glightbox" data-gallery="images-gallery">
                  <img src={image} alt="" className="img-fluid" />
                </a>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
};

export default Gallery;
