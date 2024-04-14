import React from 'react';

const TeamMember = ({ name, email, imageUrl }) => (
  <div className="flex items-center justify-center mb-8">
    <img src={imageUrl} className="shadow object-cover rounded-full w-24 h-24 mr-4" alt={name} />
    <div>
      <p className="text-lg font-semibold">{name}</p>
      <p className="text-sm text-gray-600">{email}</p>
    </div>
  </div>
);

const AboutPage = () => (
  <div className="font-VarelaRound min-h-screen">
    <div className="container mx-auto py-8">
      <div className="bg-white rounded-lg shadow-xl p-10">
        <h1 className="text-3xl font-bold text-gray-900 text-center mb-8">Our Team</h1>
        <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
          <TeamMember
            name="Zach Carlson"
            email="carlsozl@mail.uc.edu"
            imageUrl="https://media.licdn.com/dms/image/C4D03AQFjfbtVVoh2Ug/profile-displayphoto-shrink_400_400/0/1580411924609?e=1717632000&v=beta&t=dR7ynyEAFP6UeEf0ABBaYZKXHWE5zXG-FEcpLkaK5Yk"
          />
          
          <TeamMember
            name="Jake D'Amico"
            email="damicojb@mail.uc.edu"
            imageUrl="https://media.licdn.com/dms/image/D5603AQEIrIKWJ_sH-A/profile-displayphoto-shrink_400_400/0/1687204261723?e=1717632000&v=beta&t=2sP393ydrd5xdOIRhcDX7TDheG1vsR5SRlaXaDcj1wo"
          />

          <TeamMember
            name="Sean Tarbuck"
            email="tarbucsm@mail.uc.edu"
            imageUrl="https://media.licdn.com/dms/image/C5603AQF_lx1YQg5j5Q/profile-displayphoto-shrink_400_400/0/1597340834352?e=1717632000&v=beta&t=BVEOAZUXBrHP662yFMdAe_qUVa0vpip66xunACgE3cQ"
          />

          <TeamMember
            name="Rylee Charlton"
            email="charltrj@mail.uc.edu"
            imageUrl="https://media.licdn.com/dms/image/C4E03AQFwTe5ytbVDVw/profile-displayphoto-shrink_400_400/0/1556304353547?e=1717632000&v=beta&t=i4pNNykZScHqi3BcSCqfMa8e-SOK0DBHpyoEc1DDPMs"
          />

        </div>
      </div>
      <div className="mt-12 bg-white rounded-lg shadow-xl p-8">
      <div className="mt-0 mr-auto mb-10 ml-auto max-w-xl md:mx-auto sm:text-center lg:max-w-2xl md:mb-12">
              <div></div>
              <div className="mt-0 mr-auto mb-6 ml-auto font-bold leading-none text-gray-900 text-3xl max-w-lg font-VarelaRound
                  tracking-tight sm:text-4xl md:mx-auto">
                <div className="relative inline-block">
                  
                  <p className="font-bold leading-none text-gray-900 text-3xl relative max-w-lg font-VarelaRound tracking-tight
                      sm:text-4xl md:mx-auto inline">Learn More about 
                      </p>
                  <p className="font-bold leading-none text-blue-600 font-VarelaRound text-3xl relative max-w-lg font-VarelaRound tracking-tight
                      sm:text-4xl md:mx-auto ">Precise Picks!</p>
                </div>
                <p className="inline"></p>
              </div>
              <p className="text-gray-700 text-base md:text-lg font-VarelaRound">Join us on this exciting venture into the future of sports
                  betting with Precise Picks!</p>
            </div>
      </div>
      {/* Other sections of the About page */}
      <div className="mt-12 grid gap-12 lg:grid-cols-3">
        <div className="bg-white rounded-lg shadow-xl p-8">
          <img src="https://icons.veryicon.com/png/o/miscellaneous/alicloud-official-website/benefits.png" alt="Benefits Image" className="h-10 w-10 mb-4 mx-auto" />
          <p className="text-center mt-0 mr-auto mb-3 ml-auto font-extrabold text-2xl max-w-xs
              font-VarelaRound">Benefits:</p>
          <p className="mt-0 mr-auto mb-2 ml-auto text-gray-700 max-w-xs font-VarelaRound">Discover how Precise Picks can elevate
              your sports betting experience. With the burgeoning expansion of the sports betting market, fueled
              by the widespread legalization of betting, online platforms have become increasingly prominent.
              Leveraging cutting-edge algorithms that integrate data from credible sources, sports betting
              websites offer users a competitive advantage. This data-driven approach empowers users to make
              well-informed betting decisions, leading to heightened prediction accuracy, increased success rates,
              and the potential for greater profits.</p>
        </div>
        {/* Section 2 */}
        <div className="bg-white rounded-lg shadow-xl p-8">
          <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/55/Magnifying_glass_icon.svg/1024px-Magnifying_glass_icon.svg.png" alt="Key Highlights Image" className="h-6 w-6 mb-8 mx-auto" />
          <p className="text-center mt-0 mr-auto mb-3 ml-auto font-extrabold text-2xl max-w-xs font-VarelaRound">Key Highlights:</p>
          <p underline="false" className="text-left font-semibold font-VarelaRound">Algorithmic Precision:</p>
          <p className="mt-0 mr-auto mb-2 ml-auto text-gray-700 max-w-xs font-VarelaRound">&nbsp;Our platform employs sophisticated
              algorithms to analyze data from reputable sources, ensuring precision in predictions.</p>
          <p underline="false" className="text-left font-semibold font-VarelaRound">Transparency and Trust:</p>
          <p className="mt-0 mr-auto mb-2 ml-auto text-gray-700 max-w-xs font-VarelaRound">By utilizing trustworthy data sources, we
              prioritize transparency and foster user trust, enhancing the overall betting experience.</p>
          <p underline="false" className="text-left font-semibold font-VarelaRound">Accessibility:</p>
          <p className="mt-0 mr-auto mb-2 ml-auto text-gray-700 max-w-xs font-VarelaRound">Access our predictions on-the-go through
              user-friendly mobile applications, providing convenience and flexibility.</p>
        </div>
        {/* Section 3 */}
        <div className="bg-white rounded-lg shadow-xl p-8">
          <img src="https://static.thenounproject.com/png/2010152-200.png" alt="Machine Learning and AI Image" className="h-8 w-8 mb-6 mx-auto" />
          <p className="text-center mt-0 mr-auto mb-3 ml-auto font-extrabold text-2xl max-w-xs
              transition-colors duration-200  font-VarelaRound">Our Goals in Machine Learning and AI:</p>
          <p className="mt-0 mr-auto mb-2 ml-auto text-gray-700 max-w-xs font-VarelaRound">Embark on a journey into the realms of
              Machine Learning and Artificial Intelligence with our project. Our primary goal is to develop a
              machine-learned model using Python, specifically designed to analyze sports statistics and generate
              accurate predictions. These predictions will serve as the foundation for an interactive website,
              allowing users to access insights that can influence their future bets. Our project emphasizes both
              practical results and the educational aspects, offering users a comprehensive understanding of the
              intricate world of Machine Learning and AI.</p>
        </div>
      </div>
      {/* Contact Form */}
      <div className="mt-12 bg-white rounded-lg shadow-xl p-8">
      <form>
            <div fontFamily="Montserrat" className="mb-4">
              <label htmlFor="name" className="text-2xl font-bold mb-2 block">Contact Us!</label>
              <label htmlFor="name" className="text-gray-700 text-sm font-bold mb-2 block">Name</label>
              <input type="text" placeholder="Enter your name" className="focus:border-indigo-700 focus:outline-none
                  focus:shadow-outline flex-grow transition duration-200 appearance-none p-2 border-2 border-gray-300
                  text-black bg-gray-100 font-normal w-full h-12 text-xs rounded-md shadow-sm" id="name"/>
            </div>
            <div className="mb-4">
              <label htmlFor="email" className="text-gray-700 text-sm font-bold mb-2 block">Email</label>
              <input type="email" placeholder="Enter your email" className="focus:border-indigo-700 focus:outline-none
                  focus:shadow-outline flex-grow transition duration-200 appearance-none p-2 border-2 border-gray-300
                  text-black bg-gray-100 font-normal w-full h-12 text-xs rounded-md shadow-sm" id="email"/>
            </div>
            <div className="mb-4">
              <label htmlFor="message" className="text-gray-700 text-sm font-bold mb-2 block">Message</label>
              <textarea type="textarea" placeholder="Enter your message" className="text-black bg-gray-100 font-normal
                  w-full h-32 text-xs rounded-md shadow-sm focus:border-indigo-700 focus:outline-none
                  focus:shadow-outline flex-grow transition duration-200 appearance-none p-2 border-2 border-gray-300"
                  id="message"></textarea>
            </div>
            <div className="items-center justify-between flex">
              <button type="submit" className="inline-flex border border-black focus:outline-none
                  focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2 border-black font-bold justify-center
                  rounded-md py-2 px-4 bg-blue-300 text-sm text-black shadow-sm mb-10">Submit</button>
            </div>
          </form>
      </div>
    </div>
  </div>
);

export { AboutPage };
