#!/usr/bin/env python3
"""
Spaceship Builder

Learning goals:
- Class definitions with __init__
- Inheritance: Component -> Engine/Weapon/Shield
- Composition: a Ship "has a" Hull and Components
- Methods that operate on object state
- Very small text UI
"""

# ---------------------------
# Model (very small & readable)
# ---------------------------

class Hull:
    """
    A Ship must have exactly one Hull.
    The hull only tracks a name and how many component slots it has.
    """
    def __init__(self, name, slots):
        self.name = name
        self.slots = slots

    def summary(self):
        return f"{self.name} (slots: {self.slots})"


class Component:
    """
    Base class for all components.
    Subclasses only add one 'stat' field to keep it very simple.
    """
    def __init__(self, name):
        self.name = name

    def kind(self):
        # self.__class__ means "what class is this object an instance of?"
        # Example: if self is an Engine, then self.__class__ is Engine
        #
        # __name__ gives us the *name* of that class as a string.
        # Example: Engine.__name__ is the string "Engine"
        #
        # So this line will return the class name of the current object.
        return self.__class__.__name__

    def summary(self):
        # Here we call kind() to print the class name (like "Engine" or "Weapon"),
        # followed by the component's name (like "Ion-90 Engine").
        return f"{self.kind()}: {self.name}"




# Each of these classes (Engine, Weapon, Shield) extends the base class "Component".
# That means they "inherit" from Component: they automatically get its variables
# (like self.name) and methods (like kind()), but they can also add new variables
# and override methods to customize behavior.

class Engine(Component):
    def __init__(self, name, thrust):
        # super() means "go up to the parent class"
        # In this case, Engine's parent class is Component.
        #
        # Component has its own __init__ method:
        #     def __init__(self, name):
        #         self.name = name
        #
        # By calling super().__init__(name),
        # we are *reusing* that code so we don’t have to write "self.name = name" again here.
        #
        # Without this call, the Engine object would not have self.name set up!
        super().__init__(name)

        # Now we add the Engine-specific attribute.
        # This is unique to Engine, so it is written here instead of in Component.
        self.thrust = thrust  # measured in kilonewtons (kN)


    # Override the summary() method so that Engines display their thrust
    def summary(self):
        return f"{self.kind()}: {self.name} (thrust: {self.thrust} kN)"


class Weapon(Component):
    def __init__(self, name, dps):
        # Reuse Component's constructor to set self.name
        super().__init__(name)
        # Add a new attribute specific to Weapon
        self.dps = dps  # damage per second

    # Override the summary() method so Weapons display their dps
    def summary(self):
        return f"{self.kind()}: {self.name} (dps: {self.dps})"


class Shield(Component):
    def __init__(self, name, capacity):
        # Again, call Component's constructor to set self.name
        super().__init__(name)
        # Add a new attribute specific to Shield
        self.capacity = capacity  # shield capacity in some units (e.g., MJ)

    # Override the summary() method so Shields display their capacity
    def summary(self):
        return f"{self.kind()}: {self.name} (capacity: {self.capacity})"

class Ship:
    """
    A Ship has a name, one hull, and a list of components.
    We enforce only one simple rule: you can't exceed the hull's slot count.
    """
    def __init__(self, name):
        self.name = name
        self.hull = None
        self.components = []

    def set_hull(self, hull):
        self.hull = hull
        # If the new hull has fewer slots than current components,
        # we *do not* remove components (kept simple). Students can extend this.
        print(f"[+] Hull installed: {hull.summary()}")

    def slots_used(self):
        return len(self.components)

    def slots_free(self):
        if self.hull is None:
            return 0
        return max(self.hull.slots - self.slots_used(), 0)

    def add_component(self, component):
        if self.hull is None:
            print("[!] Install a hull first.")
            return False
        if self.slots_used() >= self.hull.slots:
            print("[!] No free slots left on this hull.")
            return False
        self.components.append(component)
        print(f"[+] Added: {component.summary()}")
        return True

    def remove_last_component(self):
        if not self.components:
            print("[!] No components to remove.")
            return
        removed = self.components.pop()
        print(f"[-] Removed: {removed.summary()}")

    def total_thrust(self):
        return sum(c.thrust for c in self.components if isinstance(c, Engine))

    def total_dps(self):
        return sum(c.dps for c in self.components if isinstance(c, Weapon))

    def total_shield(self):
        return sum(c.capacity for c in self.components if isinstance(c, Shield))

    def spec_sheet(self):
        lines = []
        lines.append(f"=== SHIP: {self.name} ===")
        if self.hull is None:
            lines.append("Hull: (none)")
        else:
            lines.append(f"Hull: {self.hull.summary()}")
        lines.append(f"Slots used: {self.slots_used()}" + (f"/{self.hull.slots}" if self.hull else ""))

        if not self.components:
            lines.append("Components: (none)")
        else:
            lines.append("Components:")
            for i, c in enumerate(self.components, start=1):
                lines.append(f"  {i:02d}. {c.summary()}")

        # Tiny roll-up stats for fun
        lines.append("")
        lines.append(f"Totals -> Thrust: {self.total_thrust()} kN | DPS: {self.total_dps()} | Shield: {self.total_shield()}")
        return "\n".join(lines)

    def ascii_schematic(self):
        """
        Very simple text 'diagram'. Students can easily edit this.
        """
        title = f"{self.name} - {self.hull.summary() if self.hull else 'No Hull'}"
        width = max(40, len(title) + 4)
        top = "+" + "-" * (width - 2) + "+"
        lines = [top, "|" + title.center(width - 2) + "|", "|" + " " * (width - 2) + "|"]


        engines = []  # start with an empty list
        for c in self.components:                  # go through each component in the ship
            if isinstance(c, Engine):              # check if this component is an Engine
                engines.append(c.name)             # if yes, add its name to the engines list

        weapons = []  
        for c in self.components:
            if isinstance(c, Weapon):              # check if it's a Weapon
                weapons.append(c.name)             # add the weapon's name

        shields = []
        for c in self.components:
            if isinstance(c, Shield):              # check if it's a Shield
                shields.append(c.name)             # add the shield's name



        def section(label, items):
            lines.append("|" + f"[{label}]".ljust(width - 2) + "|")
            if items:
                text = ", ".join(items)
            else:
                text = "(none)"
            # simple wrap that keeps it readable
            chunk = text
            while len(chunk) > 0:
                line = chunk[:width - 4]
                chunk = chunk[width - 4:]
                lines.append("|  " + line.ljust(width - 4) + "  |")
            lines.append("|" + " " * (width - 2) + "|")

        section("ENGINES", engines)
        section("WEAPONS", weapons)
        section("SHIELDS", shields)

        lines.append(top)
        return "\n".join(lines)


# ---------------------------
# Tiny Catalog (plain data)
# ---------------------------

HULL_CATALOG = [
    Hull("Sparrow (Light)", 4),
    Hull("Kestrel (Medium)", 6),
    Hull("Condor (Heavy)", 8),
]

ENGINE_CATALOG = [
    ("Ion-90", 120),   # (name, thrust)
    ("Ion-160", 220),
    ("Vector-X", 360),
]

WEAPON_CATALOG = [
    ("Pulse Laser", 15),   # (name, dps)
    ("Railgun", 24),
    ("Plasma Arc", 35),
]

SHIELD_CATALOG = [
    ("MK-I Shield", 120),  # (name, capacity)
    ("MK-II Shield", 220),
]


# ---------------------------
# Super Small CLI
# ---------------------------

def choose_from_list(title, items):
    print(f"\n-- {title} --")
    for i, it in enumerate(items, start=1):
        # print a friendly preview
        if isinstance(it, Hull):
            print(f"  {i}. {it.summary()}")
        elif isinstance(it, tuple):
            # tuple form in component catalogs
            print(f"  {i}. {it[0]}")
        else:
            print(f"  {i}. {it}")
    print("  0. Cancel")

    while True:
        raw = input("Choose #: ").strip()
        if not raw.isdigit():
            print("Enter a number.")
            continue
        n = int(raw)
        if n == 0:
            return None
        if 1 <= n <= len(items):
            return items[n - 1]
        print("Invalid choice.")


def main():
    print("Welcome to the SIMPLE Spaceship Builder")
    name = input("Name your ship: ").strip() or "Untitled"
    ship = Ship(name)

    while True:
        print("\n==============================")
        print("1) Install/Change Hull")
        print("2) Add Engine")
        print("3) Add Weapon")
        print("4) Add Shield")
        print("5) View Ship Specs")
        print("6) View ASCII Schematic")
        print("7) Remove Last Component")
        print("0) Finish & Exit")
        print("==============================")
        choice = input("Select: ").strip()

        if choice == "1":
            h = choose_from_list("Select a Hull", HULL_CATALOG)
            if h:
                ship.set_hull(h)

        elif choice == "2":
            pick = choose_from_list("Select an Engine", ENGINE_CATALOG)
            if pick:
                name, thrust = pick
                ship.add_component(Engine(name, thrust))

        elif choice == "3":
            pick = choose_from_list("Select a Weapon", WEAPON_CATALOG)
            if pick:
                name, dps = pick
                ship.add_component(Weapon(name, dps))

        elif choice == "4":
            pick = choose_from_list("Select a Shield", SHIELD_CATALOG)
            if pick:
                name, cap = pick
                ship.add_component(Shield(name, cap))

        elif choice == "5":
            print()
            print(ship.spec_sheet())

        elif choice == "6":
            print()
            print(ship.ascii_schematic())

        elif choice == "7":
            ship.remove_last_component()

        elif choice == "0":
            print("\nFinal Specs:")
            print(ship.spec_sheet())
            print("\nSchematic:")
            print(ship.ascii_schematic())
            print("\nGoodbye.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
