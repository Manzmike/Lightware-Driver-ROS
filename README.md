<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Manzmike">
  </a>

<h3 align="center">Lightware_driver ROS2 for SF30/D (200 m) Lightware LiDAR</h3>

  <p align="center">
    This repo contains a ROS2 driver for the SF30/D (200 m) Lightware LiDAR. This package was ported to ROS2 for use in the CARMA 1tenth scaled-down cooperative driving automation program. The code has been tested in Ubuntu 20.04/ROS2 Foxy.
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With


[![ROS2-foxy][ROS2]][ROS2-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>




### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Manzmike/lightware_driver.git
   ```
2. Navigate to the root directory
   ```sh
   cd lightware_driver
   ```
3. Build the package with colcon
   ```sh
   colcon build --packages-select lightware_driver
   ```
4. Source ROS 2 in the command line
   ```sh
   . install/setup.bash
   ```   
5. Run the Lightware Driver
   ```sh
   ros2 run lightware_driver talker
   ``` 


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

To use this ROS2 driver for the Lightware SF30/D (200 m) LiDAR, first make sure that you have installed all the necessary dependencies and have built the package using colcon (see Getting Started). Once you have built the package, you can run the driver using the following command:

```sh
ros2 run lightware_driver talker
```
This will start the driver node and begin publishing point cloud data from the LiDAR. You can subscribe to the point cloud topic using another node or visualization tool, such as RViz.

Additionally, you can configure the driver by modifying the parameters in the YAML file located in the params/ directory. For example, you can adjust the maximum range or minimum intensity thresholds, or set the number of points to skip between scans. These parameters can be modified at runtime using the ros2 param command.

For more information on using ROS2 and working with LiDAR data, refer to the ROS2 documentation and LiDAR tutorials.

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Michael Lindsay - mikelindsayengineering@gmail.com

Project Link: [https://github.com/the-hive-lab/lightware_driver](hhttps://github.com/the-hive-lab/lightware_driver)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* I would like to express my deepest gratitude to Dr. Martin, my Engineering professor, for his invaluable guidance and mentorship throughout the development of this lidar driver for ROS 2 interfacing with a SF30/D (200 m) Lightware LiDAR. His expertise and insights have been instrumental in the success of this project.[]( )
* Dr. Martin's unwavering support, encouragement, and constructive feedback have been a constant source of motivation for me, and I am grateful for his willingness to share his knowledge and expertise with me. I am honored to have had the opportunity to work with such a dedicated and knowledgeable professor, and I am confident that the skills and knowledge I have gained under his tutelage will serve me well in my future endeavors.[]()
* Once again, I would like to express my heartfelt thanks to Dr. Martin for his exceptional mentorship and guidance.[]()

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/github_username/repo_name.svg?style=for-the-badge
[contributors-url]: https://github.com/github_username/repo_name/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/github_username/repo_name.svg?style=for-the-badge
[forks-url]: https://github.com/github_username/repo_name/network/members
[stars-shield]: https://img.shields.io/github/stars/github_username/repo_name.svg?style=for-the-badge
[stars-url]: https://github.com/github_username/repo_name/stargazers
[issues-shield]: https://img.shields.io/github/issues/github_username/repo_name.svg?style=for-the-badge
[issues-url]: https://github.com/github_username/repo_name/issues
[license-shield]: https://img.shields.io/github/license/github_username/repo_name.svg?style=for-the-badge
[license-url]: https://github.com/github_username/repo_name/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/michael-l-81316a164
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[ROS2]: https://docs.ros.org/en/foxy/_static/foxy-small.png
[ROS2-url]: https://docs.ros.org/en/foxy/index.html
