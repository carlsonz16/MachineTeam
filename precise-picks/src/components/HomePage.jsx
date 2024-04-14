import React from 'react';

const HomePage = () => (
  <div className="min-h-screen font-VarelaRound">
    <div className="container mx-auto py-8">
      <div className="shadow-lg rounded-lg bg-white p-20">
        <div className="flex flex-col md:flex-row">
          <div className="w-full md:w-1/2 p-4">
            <img src="https://t4.ftcdn.net/jpg/00/62/39/19/240_F_62391976_WKbOA72PbU28IAfUjn6tLAPz3e2IVxdr.jpg" className="object-contain object-top rounded-full w-full h-auto lg:h-auto lg:w-5/6 mr-auto ml-auto"/>
          </div>
          <div className="w-full md:w-1/2 p-4">
            <div className="text-center md:text-left">
              <h1 className="text-3xl font-bold text-gray-900 mb-4">Welcome to <span className="text-blue-600">Precise Picks!</span></h1>
              <p className="text-gray-700 text-lg mb-4">The sports betting market has seen rapid expansion due to the increased legalization of betting in multiple regions. This growth has been fueled by the emergence of online platforms, advanced technologies, and the.....</p>
              <a href="/about" className="bg-blue-700 text-white font-semibold tracking-wide py-3 px-6 rounded-md shadow-md inline-block transition duration-200 hover:bg-blue-900 focus:shadow-outline focus:outline-none">Read More...</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
);

export { HomePage };