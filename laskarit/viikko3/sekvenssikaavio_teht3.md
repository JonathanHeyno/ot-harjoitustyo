```mermaid
sequenceDiagram
  participant Main
  participant Machine
  participant FuelTank
  participant Engine
  Main->>Machine: Machine()
  Machine->>FuelTank: FuelTank()
  Machine->>FuelTank: fill(40)
  Machine->>Engine: Engine(tank)
  Main->>Machine: drive()
  Machine->Engine: start()
  Engine->FuelTank: consume(5)
  Machine->Engine: is_running()
  Engine-->FuelTank: True
  Machine->Engine: use_energy()
  Engine->FuelTank: consume(10)
```