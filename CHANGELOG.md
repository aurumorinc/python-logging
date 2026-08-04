## Breaking Changes

* **Project Rename and Restructuring**
  * Description: Renamed the entire project, modules, import paths, class names, environment variables, and test suites from `worldline` to `python-logging`.
  * Technical Details: Updated all internal module structures and test suites.
  * Commits: [`12bcf96`](https://github.com/aurumorinc/python-logging/commit/12bcf968), [`3662ab4`](https://github.com/aurumorinc/python-logging/commit/3662ab4f), [`b3a9b8e`](https://github.com/aurumorinc/python-logging/commit/b3a9b8ec)

* **Public API and Class Name Updates (`WorldlineSettings` to `LoggingSettings`)**
  * Description: Renamed public classes, specifically `WorldlineSettings`, to `LoggingSettings`, along with associated environment variables and configuration files.
  * Migration Path: 
    * Update all import statements in your codebase:
      ```python
      # Before
      from worldline import WorldlineSettings

      # After
      from python_logging import LoggingSettings
      ```
    * Rename all references of the `WorldlineSettings` class to `LoggingSettings`.
    * Update any environment variables and configuration files associated with the old package name to align with the new `python-logging` naming convention.
