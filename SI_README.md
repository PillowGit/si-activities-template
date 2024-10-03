# How to create a new activity for your students:

1. Add a folder that has the name of the activity you want. This can be
something like `session-1` or `linked_lists`.

2. Place whatever related files you want inside of that folder, make sure the `run.sh` file is copied into it aswell from the example activity.

3. Come up with a single, one line command that compiles your activity how
you'd like and write it down for later.

> [!TIP]
> If you want to write multiple commands, use && to join them. For example, running `clang++ ...` and `./a.out` in one line would be written as `clang++ main.cpp && ./a.out`

4. Write the activity into the `activities.yaml` file so that the run script recognizes it, use the following format:

> [!NOTE]
> The running script cd's into the folder with the matching `activity_name`, then runs the command specified in `cmd`.

```yaml
activity_name:
  cmd: "clang++ main.cpp && ./a.out"
```

5. If all works well, students should be able to use the command `./run.sh activity_name` to run their activity with your command instantly.
