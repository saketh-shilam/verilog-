# Complete Verilog HDL Repository

This repository is a comprehensive collection of Verilog HDL programs covering fundamental to advanced digital design concepts. It is designed as a structured learning and reference resource for students and aspiring VLSI engineers.

---

##  Objectives

* Build strong fundamentals in Verilog HDL
* Practice RTL design and simulation
* Prepare for VLSI/EDA interviews
* Maintain a well-organized digital design portfolio

---

##  Topics Covered

###  Basic Programs

* AND, OR, NOT, NAND, NOR, XOR gates
* Multiplexer & Demultiplexer
* Encoder & Decoder

###  Combinational Circuits

* Half Adder & Full Adder
* Half Subtractor & Full Subtractor
* Comparator
* Code Converters

###  Sequential Circuits

* SR Flip-Flop
* JK Flip-Flop
* D Flip-Flop
* T Flip-Flop

###  Counters

* 4-bit Up Counter
* 4-bit Down Counter
* Up/Down Counter
* Ring Counter
* Johnson Counter

###  Shift Registers

* SISO, SIPO, PISO, PIPO

###  FSM (Finite State Machines)

* Moore Machine
* Mealy Machine

###  Advanced Designs (Upcoming 🚀)

* ALU (Arithmetic Logic Unit)
* UART Communication
* Simple Processor Design

---

##  Tools & Software

* Verilog HDL
* Icarus Verilog (iverilog)
* GTKWave

---

##  How to Run

### Step 1: Compile

```bash
iverilog design.v testbench.v -o output
```

### Step 2: Run

```bash
vvp output
```

### Step 3: View Waveform

```bash
gtkwave dump.vcd
```

---

##  Folder Structure

```
verilog/
│── basic_gates/
│── combinational/
│── sequential/
│── counters/
│── shift_registers/
│── fsm/
│── advanced/
│── testbenches/
│── README.md
```

---

##  What You Will Learn

* Writing synthesizable Verilog code
* Designing combinational & sequential circuits
* FSM design techniques
* Simulation and debugging
* Waveform analysis

---

##  Future Improvements

* Add timing analysis
* Add synthesis reports
* Add FPGA implementation (optional)
* Include waveform screenshots

---

##  Contribution

This is a personal learning repository, but suggestions and improvements are welcome.

---

## Author

**Saketh Shilam**
GitHub: https://github.com/saketh-shilam

---

⭐ Star this repo if you find it useful!
