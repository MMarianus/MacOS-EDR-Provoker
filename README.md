<br/>
<p align="center">
  <a href="https://github.com/MMarianus/MacOS-EDR-Provoker">

  </a>

  <h3 align="center">The MacOS EDR Provoker</h3>

  <p align="center">
    A basic script to ensure an EDR is working properly on a MacOS.
    <br/>
    <br/>
  </p>
</p>

![Downloads](https://img.shields.io/github/downloads/MMarianus/MacOS-EDR-Provoker/total) ![Contributors](https://img.shields.io/github/contributors/MMarianus/MacOS-EDR-Provoker?color=dark-green) ![Forks](https://img.shields.io/github/forks/MMarianus/MacOS-EDR-Provoker?style=social) ![Stargazers](https://img.shields.io/github/stars/MMarianus/MacOS-EDR-Provoker?style=social) ![License](https://img.shields.io/github/license/MMarianus/MacOS-EDR-Provoker) 

## About The Project
<p align="center">
<img width="550" alt="image" src="https://github.com/MMarianus/MacOS-EDR-Provoker/assets/25618241/156363e2-ae34-44b8-b984-46793d7063aa">
</p>


This Python script is designed to perform four tests that should trigger EDR (Endpoint Detection and Response) detections. The tests are designed to check the detection and response capabilities of your EDR solution, helping you ensure your system's security is operative and working properly.                                            

After running the tests, observe your EDR console closely, as you might see some detections or suspicious activites in action!                                                

The tests are: 
* list users
* take a screenshot
* encrypt files 
* spawn a reverse shell                                                    

## Disclaimer
This script is intended for legitimate testing or educational purposes only. Use of this script on any system without proper authorization may lead to serious legal and ethical consequences. The script creator is not responsible for any misuse or damages caused by this script. Use it responsibly and at your own risk.

## Usage

    python3 macos-edr-provoker.py

***[WARNING]*** - This script encrypts all files within the script's folder execution

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/MMarianus/MacOS-EDR-Provoker/issues/new) to discuss it, or directly create a pull request.
* Please make sure you check your spelling and grammar.
* Please create individual PR for each suggestion.

### Creating A Pull Request

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the GNU License. See [LICENSE](https://github.com/MMarianus/MacOS-EDR-Provoker/blob/main/LICENSE) for more information.

## Authors

* [MMarianus](https://github.com/MMarianus)
