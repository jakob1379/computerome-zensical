{
  description = "Computerome wiki (Zensical)";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs =
    { nixpkgs, ... }:
    let
      inherit (nixpkgs) lib;
      forAllSystems = f: lib.genAttrs lib.systems.flakeExposed (s: f nixpkgs.legacyPackages.${s});
      zensicalFor =
        pkgs:
        let
          upstream = pkgs.python314Packages.zensical;
        in
        if upstream.version == "0.1.1" then
          upstream.overridePythonAttrs (old: rec {
            version = "0.1.2";
            src = pkgs.fetchFromGitHub {
              owner = "zensical";
              repo = "zensical";
              tag = "v${version}";
              hash = "sha256-UH9iuQUCUB6Y1N/p2/c+71PftgWgd/nJNypLkaxnhsg=";
            };
            cargoDeps = pkgs.rustPlatform.importCargoLock {
              lockFile = "${src}/Cargo.lock";
              outputHashes."zrx-0.0.27" = "sha256-hkwORGKLCdGkASguA68oZuAk24N0iXSsA7mYdIoYiLM=";
            };
          })
        else
          lib.warn "nixpkgs zensical is ${upstream.version}: remove the 0.1.2 override in flake.nix" upstream;
    in
    {
      packages = forAllSystems (pkgs: {
        default = pkgs.stdenvNoCC.mkDerivation {
          name = "computerome-wiki";
          src = pkgs.lib.fileset.toSource {
            root = ./.;
            fileset = pkgs.lib.fileset.unions [
              ./docs
              ./includes
              ./overrides
              ./zensical.toml
            ];
          };
          nativeBuildInputs = [
            (zensicalFor pkgs)
            pkgs.pngquant
          ];
          # The privacy plugin needs network to localize external fonts and scripts; the sandbox has none.
          buildPhase = ''
            sed -i 's/^\[project.plugins.privacy\]$/&\nenabled = false/' zensical.toml
            zensical build --clean --strict
          '';
          installPhase = "cp -r site $out";
        };
      });

      devShells = forAllSystems (pkgs: {
        default = pkgs.mkShell {
          packages = [
            pkgs.python314
            pkgs.uv
            pkgs.pngquant
          ];
          UV_PYTHON = "${pkgs.python314}/bin/python";
          UV_PYTHON_DOWNLOADS = "never";
        };
      });
    };
}
