# 🚀 Git Workflow Guide (DataNexus Project)

## 🧠 Branch Structure

* `main` → stable / production-ready code
* `development` → active work happens here

---

## 🔥 Daily Workflow

### 1. Switch to development branch

```bash
git checkout development
git pull
```

### 2. Do your work

* Create/edit files
* Test your code

### 3. Stage and commit changes

```bash
git add .
git commit -m "describe what you changed"
```

### 4. Push to GitHub

```bash
git push
```

---

## 🚀 Updating `main` (only when code is stable)

### 5. Switch to main

```bash
git checkout main
git pull
```

### 6. Merge development into main

```bash
git merge development
```

### 7. Push main

```bash
git push
```

### 8. Return to development

```bash
git checkout development
```

---

## ⚠️ Common Mistake

❌ Wrong:

```bash
git checkout development
git merge main
```

✅ Correct:

```bash
git checkout main
git merge development
```

---

## 🧪 Handling Merge Conflicts

If you see a conflict:

```text
your code
```

### Fix Steps:

1. Open the file in VS Code
2. Manually resolve the conflict
3. Run:

```bash
git add .
git commit -m "resolved merge conflict"
git push
```

---

## 🧼 Simple Rule

* Work in `development`
* Stable code goes to `main`
* Always merge: `development → main`
