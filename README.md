# 🌌 SpectraCLI – Build Beautiful Animated CLIs in Minutes

SpectraCLI is a lightweight Python framework that lets you create **colorful, animated, interactive CLI applications** with almost _no code_.

Define your commands in a simple `cli.json` file, and SpectraCLI handles:

✨ colors
✨ banners
✨ spinners
✨ progress bars
✨ tables
✨ prompts
✨ command routing
✨ error handling
✨ clean UI

Perfect for tools, demos, scripts, or small terminal utilities.

---

## 🚀 Features

- 🎨 **Full Color API** (red, green, magenta, cyan, etc.)
- 💫 **ASCII Art Banners** using `pyfiglet`
- 🔄 **Spinners / Loading Animations**
- 📊 **Progress Bars**
- 📝 **Interactive Prompts**
- ❓ **Yes/No Confirmations**
- 📋 **Table Rendering**
- 🧹 **Clear Screen Support**
- 🧩 **JSON-Based Command Definitions**
- 🔐 Safe command execution (isolated env)
- 🔧 Built-in `help` command

No boilerplate. No setup.
Just pure CLI drip.

---

## 📦 Installation

### 1. Install Dependencies

```sh
pip install colorama pyfiglet
```

### 2. Clone SpectraCLI

```sh
git clone https://github.com/NightNovaNN/SpectraCLI
cd SpectraCLI
```

---

## 🛠️ Usage

Create a file named `cli.json`:

```json
{
  "name": "SpaceTool",
  "banner": true,
  "banner_color": "cyan",
  "commands": {
    "launch": "s=Spinner('Launching rocket','yellow');s.start();time.sleep(2);s.stop('Rocket launched!')",
    "progress": "progress(30,0.03,'green')",
    "hello": "print(color('Hello, Universe!','magenta'))",
    "askname": "n=ask('Your name?');print(color('Hello '+n,'cyan'))",
    "tabletest": "table(['Planet','Mass'],[['Earth','5.97e24'],['Mars','6.39e23']])",
    "clear": "clear()"
  }
}
```

Run:

```sh
python spectra.py
```

---

## 🎮 Example Output

### Startup

```sh
SpectraCLI Loaded: SpaceTool
```

### Commands

```sh
> hello
Hello, Universe!

> launch
| Launching rocket
/ Launching rocket
✔ Rocket launched!

> progress
[##########----------] 50%

> askname
Your name? > INN
Hello INN

> tabletest
Planet | Mass
--------------------
Earth  | 5.97e24
Mars   | 6.39e23

> exit
Exiting...
```

---

## 🧱 API Reference

### 🎨 `color(text, color)`

Colors supported:
`red, green, blue, yellow, cyan, magenta, white, gray`

### 💫 `Spinner(message, color)`

```py
s = Spinner("Loading...", "yellow")
s.start()
s.stop("Done!")
```

### 📊 `progress(total, delay, color)`

```py
progress(20, 0.05, "cyan")
```

### 📝 `ask(prompt)`

```py
name = ask("Enter name")
```

### ❓ `yesno(prompt)`

Returns `True` or `False`.

### 📋 `table(headers, rows)`

```py
table(["A","B"], [[1,2],[3,4]])
```

### 🧹 `clear()`

Clears terminal screen.

---

## 🧩 CLI Structure

SpectraCLI runs commands inside a safe execution environment with:

- color functions
- Spinner class
- progress bar
- time module
- prompts
- tables
- clear()

You can define commands inline in JSON as Python expressions.

---

## 🟢 Roadmap

- [ ] Add plugin system
- [ ] Add theming support
- [ ] Add command aliasing
- [ ] Add command arguments
- [ ] Add file-based script commands
- [ ] Add built-in help auto-formatting
- [ ] Add packaged PyPI release

---

## 🪐 Why SpectraCLI?

Because CLIs don’t have to be boring.
SpectraCLI brings **color, movement, and personality** to your tools —
making them fun to build and beautiful to use.

---

## 🤝 Contributing

Pull requests are welcome!
New animations, themes, or UI elements are appreciated.

---

## ⭐ License

MIT License.

---
