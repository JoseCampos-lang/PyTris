{
  description = "Tetris Pygame for School";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/?ref=nixos-24.11";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs =
    { nixpkgs, flake-parts, ... }@inputs:
    flake-parts.lib.mkFlake { inherit inputs; } {
      systems = [
        "x86_64-linux"
      ];

      perSystem =
        { system, ... }:
        let
          pkgs = import nixpkgs {
            inherit system;
          };
          inherit (pkgs)
            mkShell
            stdenv
            fetchFromPypi
            fetchFromGitHub
            ;
          venvpkg = with pkgs.python312Packages; [
            setuptools
            wheel
            venvShellHook
            pip
            pygame
            pygame-gui
            meson-python
          ];
        in
        {
          devShells.default = mkShell {
            buildInputs =
              with pkgs;
              [
                pkg-config
              ]
              ++ venvpkg;
            venvDir = ".venv";
          };
        };
    };
}
