# PC components
- motherboard
- processor
- RAM
- case/ chassis
- power supply
- hard drive
- peripherals


# Processor
    aka CPU, microprocessor
    major companies are intel and AMD
    386 processor was the first 32

- intel created first microprocessor in 1971 with introduction of the 4004 chip.
- process determined @bus size, clock speed, instruction efficiency. IBM proposed the iCOMP to deteermine the performance.
- features
    + Data I/O buus
        * speed and width important, defines rate of data transmission (the bandwidth). 8-->64 bits wide
    + Address bus
        * set of wires that carries addressing information  to describe memory location to which data being seent or from which data is being received. 
        * the width of the address bus indicates teh maxamount of ram a chip can access
        * the address and data bus are independent, chip designers use whatever ssize for each. however @larger data bus == larger address bus. 
    + internal registers (the inteernal data bus)
        * size of internal registers tells how much info the processor can operate on at one time
        * reigster is holding cell within processor
        * the register size also deermines the type of software/ commands teh chip can run.
        * now have internal 32 and 64 bit registers, compatibility mode allows 32 bit programs to be run
        * a 32 bit machine can only address the first 4 gigabytes of memory
    + ccache memory 
        * high speed memory buffer that temp stores data that the processor is likely going to need in teh near future.
        * differs from a buffer
        * improves speed @RAM is much slower than the CPU, cache memory prevens from having to wait.
        * levels
            - L1 cache and controller. built into the processor die. runs at the full core speed of the processor internally. the controller is the 'brain' of the cache that predicts what items are going to be requested inn teh cache a cache miss is when the cache controller did not correctly fill the cache with thee data the procesor actually needed.
    + multicore technology
        * contains 2 or more physical processor cores in a single processor package, rather than just simulating the cores using hyperthreading (can simulate multiple cores at the cost of some speed)
        * first dual core x86 compatible desktop processor 2005 by AMD and Intel. first quad core in 2006. 
        * multicore does not improve single task performance much, but more and more games designed to be multithreaded. 
    + pin grade array (PGA). grid like array of pins on teh bottom fo the package. they are inserted into socket (zero insertion force design). 
- processor speed 
    + often misunderstood
    + clock speed set @Crystal oscillator
    + wait states are when nothing happens so that the processor does not get ahead of the erest of the computer.
    + cycles per instruction has decreased -- @8088 old processors took 12 cycles on average to execute one instruction. now many intrusctions per cycle with multi core cpus. the 1GHz clock speed was surpasseed in 2000.
    + it is about the  architecture not necessarily the Hz of a processor that determines its speed. @instruction efficienccy. eg the old 133 MHz processor were slower than the 75 Hz pentium
- heatsink
    + special attahcment for chip to draw heat away. been necessary since 1990s with pentium processors. conducts heat away with metal thermal conductor. 
    + are rated for their cooling perforamnces
    + an active heatsink is one that incorporates fans
- manufacture
    + manufactured @silicon, 2nd most common element on teh planet. 2nd to oxygen. wafers produced with photolithography, creating the signal pathyways and transistors. 

# Frequency timing generator
- FTG - frequency timing generator
- coordinates the clock with the CPU to solve compatbility issues.
- 


# Crystal oscillator
- sets the computers clock speed of the processor, alternating current @voltage applied to the crytsal.  billions of cycles per second @current computers. thus measured in gigahertz. 
- overclocking  
    + set in BIOS. originally automatically determined
    + this allows to increaset he clock speed until the sysetm becomes unstable. can find the maximum sustainable speed for the system. 
- main component controlling speed is quartz crystal. SiO2 in crystalline form. 
- piezoelectric == gnerates a current when exposed to mechanical stress. 
- the sliver of quartz insie the package is usu disc shaped, %shaped like tuning fork. the quartz disc inside has electrodes on each side, allowing a voltage to be applied to teh disc
- usu have multiple oscillators @modern computers. at least 2 crystals, main cyrstal used to control spee of mobo, other used to control RTC. RTC separate clock since 1984
    + main crystal at 14.3 Mhz
    + RTC set at 32.8 KHz

# Motherboard parts
    aka mainboard
- PCI slot (peripheral component interconnect). aka conventional PCI
    + either 32/ 64 bits, connects hardwware devices to mobo. 
- system bus
    + 
- nonvolatile BIOS memory
    + small memory on pc mobo used to store BIOS settings. 
    + volatile CMOS RAM, powered by the CMOS battery to store the data. after system loses power does not store the settings.
    + the CMOS battery lasts for 10 years. most common version is the CR2032 3V battery
    + lithium battery is not rechargeable
    + @replace the lithium battery == system tiume and BIOS settings return to default.
- BIOS chips
    + basic input output system chips
    + non volatile firmware that perfrosm hardware intiialisation during booting process.
    + preinstaalled on the mobo.
    + first software to run @power on.
- south bridge
    + one of teh two chips in teh core logic chipset on a PC motherboard.
    + implements slower capabilities of the motherboard
    + not directly connected to the CPU
    + northbridge tiees the CCPU to southbridge
- north bridge
    + aka host bridge. northbridge directly connected to cpu via the front side bus. 
    + 

# Terms
- CMOS
    + complementary metal oxide semiconductor
- board managemnet controller