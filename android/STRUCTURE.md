# AOSP 仓库结构概览（android.googlesource.com）

- 生成时间：见文件 mtime
- 仓库总数：3128
- 状态统计：ok=2471; empty_ok=636; restricted=21

## 1. 顶层前缀分组
| 前缀 | 仓库数 | 说明(代表仓库 README) |
|---|---|---|
| platform | 2564 | Bug: 236926434 |
| kernel | 204 | Bug: 182962583 |
| device | 199 | Bug: 122486287 |
| toolchain | 92 | Android Rust Toolchain For the latest version of this doc, p |
| trusty | 40 | For ACL only |
| tools | 8 | A project to collect and display stats about AOSP. |
| external | 2 | Bug: 275074143 |
| mirror | 2 | Manifest that contains all the projects that are hosted on t |
| product | 2 | - |
| Kernel-Projects | 1 | - |
| Platform-Chromium-Projects | 1 | Parent projects for all projects with suffix platform/extern |
| Platform-Packages-Modules-Projects | 1 | Bug: 232410097 |
| Platform-Projects | 1 | Base project for all active Android platform projects, conta |
| Platform-Unrestricted-Projects | 1 | Base project for Android platform where all platform maintai |
| Public-Projects | 1 | - |
| accessories | 1 | - |
| assets | 1 | Bug: 32992167 |
| brillo | 1 | - |
| cts_drno_filter | 1 | Parent project for CTS projects that requires Dr.No +2's. |
| kkernel | 1 | Bug: 177597234 |
| pdk_review_filter | 1 | - |
| superprojects | 1 | - |
| tee | 1 | KeyMint reference implementation for OP-TEE This repository  |
| third-party-review | 1 | - |

## 2. Rust 相关仓库（信号初筛）
- 强信号（.rs/Cargo.toml/rustfmt/rust 目录）仓库数：496

| repo | 信号 | 说明 |
|---|---|---|
| device/google/cuttlefish | androidbp,rustfmt | Note For all host tools development please refer t |
| kernel/common | rust_dir | How do I submit patches to Android Common Kernels  |
| platform/build/soong | androidbp,rust_dir | Soong Soong is one of the build systems used in An |
| platform/development | androidbp,rustfmt | Platform engineering tools, sample code |
| platform/external/avb | androidbp,rust_dir | Android Verified Boot 2.0 This repository contains |
| platform/external/bazelbuild-rules_rust | rust_dir | Rust Rules Postsubmit Overview This repository pro |
| platform/external/crosvm | androidbp,cargo | crosvm - The ChromeOS Virtual Machine Monitor cros |
| platform/external/flatbuffers | androidbp,rust_dir | FlatBuffers FlatBuffers is a cross platform serial |
| platform/external/gsc-utils | androidbp,rust_dir | Bug: 361398570 |
| platform/external/libchromeos-rs | androidbp,cargo | libchromeos-rs - The Rust crate for common Chrome  |
| platform/external/libdrm | androidbp,rust_dir | - |
| platform/external/mesa3d | androidbp,rustfmt | - |
| platform/external/minigbm | androidbp,rust_dir | - |
| platform/external/minijail | androidbp,rust_dir | Minijail The Minijail homepage is https://google.g |
| platform/external/n2 | androidbp,cargo,rs_file | n2, an alternative ninja implementation n2 (pronou |
| platform/external/python/bumble | androidbp,rust_dir | _ _ _ / / / / / / / /__ _ _ ____ / /__ / / _____ / |
| platform/external/rust/crabbyavif | androidbp,cargo,rs_file | Crabby Avif 🦀 Avif parser/decoder implementation i |
| platform/external/rust/crates/aarch64-paging | androidbp,cargo | aarch64 page table manipulation This crate provide |
| platform/external/rust/crates/acpi | androidbp,cargo | Acpi Documentation ( rsdp ) Documentation ( acpi ) |
| platform/external/rust/crates/ahash | androidbp,cargo,rs_file,rustfmt | aHash AHash is the fastest , DOS resistant hash cu |
| platform/external/rust/crates/aho-corasick | androidbp,cargo,rustfmt | aho-corasick A library for finding occurrences of  |
| platform/external/rust/crates/android_log-sys | androidbp,cargo | Bindings to Android log Library License Licensed u |
| platform/external/rust/crates/android_logger | androidbp,cargo | Send Rust logs to Logcat This library is a drop-in |
| platform/external/rust/crates/anes | androidbp,cargo | ANSI Escape Sequences provider & parser A Rust lib |
| platform/external/rust/crates/annotate-snippets | androidbp,cargo | annotate-snippets annotate-snippets is a Rust libr |
| platform/external/rust/crates/anyhow | androidbp,cargo,rs_file | Anyhow ¯\_(°ペ)_/¯ This library provides anyhow::Er |
| platform/external/rust/crates/arbitrary | androidbp,cargo | About The Arbitrary crate lets you construct arbit |
| platform/external/rust/crates/arc-swap | androidbp,cargo,rustfmt | ArcSwap This provides something similar to what Rw |
| platform/external/rust/crates/argh | androidbp,cargo | Argh Argh is an opinionated Derive-based argument  |
| platform/external/rust/crates/argh_derive | androidbp,cargo | Argh Argh is an opinionated Derive-based argument  |
| platform/external/rust/crates/argh_shared | androidbp,cargo | Argh Argh is an opinionated Derive-based argument  |
| platform/external/rust/crates/arrayvec | androidbp,cargo | arrayvec OR A vector with fixed capacity. Please r |
| platform/external/rust/crates/ash | androidbp,cargo,rs_file | Ash A very lightweight wrapper around Vulkan Overv |
| platform/external/rust/crates/asn1-rs | androidbp,cargo | BER/DER Parsers/Encoders A set of parsers/encoders |
| platform/external/rust/crates/asn1-rs-derive | androidbp,cargo | Bug: 312436720 |
| platform/external/rust/crates/asn1-rs-impl | androidbp,cargo | Bug: 312436741 |
| platform/external/rust/crates/async-stream | androidbp,cargo | Asynchronous streams for Rust Asynchronous stream  |
| platform/external/rust/crates/async-stream-impl | androidbp,cargo | Bug: 180537538 |
| platform/external/rust/crates/async-task | androidbp,cargo | async-task Task abstraction for building executors |
| platform/external/rust/crates/async-trait | androidbp,cargo,rs_file | Async trait methods The initial round of stabiliza |
| platform/external/rust/crates/atomic | androidbp,cargo | Generic Atomic<T> for Rust A Rust library which pr |
| platform/external/rust/crates/atty | androidbp,cargo,rustfmt | atty are you or are you not a tty? install Add the |
| platform/external/rust/crates/axum | androidbp,cargo,rs_file | axum axum is a web application framework that focu |
| platform/external/rust/crates/axum-core | androidbp,cargo,rs_file | axum-core Core types and traits for axum. More inf |
| platform/external/rust/crates/base64 | androidbp,cargo | base64 Made with CLion. Thanks to JetBrains for su |
| platform/external/rust/crates/bencher | androidbp,cargo,rs_file | Bug: 175869081 |
| platform/external/rust/crates/bincode | androidbp,cargo | Bincode A compact encoder / decoder pair that uses |
| platform/external/rust/crates/bindgen | androidbp,cargo,rs_file | bindgen bindgen automatically generates Rust FFI b |
| platform/external/rust/crates/bindgen-cli | androidbp,cargo,rs_file | bindgen bindgen automatically generates Rust FFI b |
| platform/external/rust/crates/bit_field | androidbp,cargo | bit_field A simple crate which provides the BitFie |
| platform/external/rust/crates/bitflags | androidbp,cargo | bitflags bitflags generates flags enums with well- |
| platform/external/rust/crates/bitreader | androidbp,cargo | BitReader BitReader is a helper type to extract st |
| platform/external/rust/crates/bstr | androidbp,cargo,rustfmt | bstr This crate provides extension traits for &[u8 |
| platform/external/rust/crates/buddy_system_allocator | androidbp,cargo | buddy_system_allocator An (almost) drop-in replace |
| platform/external/rust/crates/bytemuck | androidbp,cargo,rustfmt | Latest Docs.rs Here bytemuck A crate for mucking a |
| platform/external/rust/crates/bytemuck_derive | androidbp,cargo | bytemuck_derive Derive macros for bytemuck traits. |
| platform/external/rust/crates/byteorder | androidbp,cargo,rustfmt | byteorder This crate provides convenience methods  |
| platform/external/rust/crates/bytes | androidbp,cargo | Bytes A utility library for working with bytes. Do |
| platform/external/rust/crates/camino | androidbp,cargo,rs_file,rustfmt | camino - UTF-8 paths This repository contains the  |
| platform/external/rust/crates/cast | androidbp,cargo | cast Ergonomic, checked cast functions for primiti |
| platform/external/rust/crates/cbindgen | androidbp,cargo,rs_file | cbindgen Read the full user docs here! cbindgen cr |
| platform/external/rust/crates/cesu8 | androidbp,cargo | CESU-8 encoder/decoder for Rust Documentation . Co |
| platform/external/rust/crates/cexpr | androidbp,cargo,rustfmt | Bug: 154342253 |
| platform/external/rust/crates/cfg-if | androidbp,cargo | cfg-if Documentation A macro to ergonomically defi |
| platform/external/rust/crates/chrono | androidbp,cargo,rustfmt | Chrono : Timezone-aware date and time handling Chr |
| platform/external/rust/crates/ciborium | androidbp,cargo | ciborium Welcome to Ciborium! Ciborium contains CB |
| platform/external/rust/crates/ciborium-io | androidbp,cargo | ciborium-io Simple, Low-level I/O traits This crat |
| platform/external/rust/crates/ciborium-ll | androidbp,cargo | ciborium-ll Low level CBOR parsing tools This crat |
| platform/external/rust/crates/clang-sys | androidbp,cargo,rs_file | clang-sys Rust bindings for libclang . If you are  |
| platform/external/rust/crates/clap | androidbp,cargo | clap Command Line Argument Parser for Rust Dual-li |
| platform/external/rust/crates/clap_complete | androidbp,cargo | clap_complete Shell completion generation for clap |
| platform/external/rust/crates/clap_derive | androidbp,cargo | clap_derive Macro implementation for clap's derive |
| platform/external/rust/crates/clap_lex | androidbp,cargo | clap_lex Minimal, flexible command line parser Dua |
| platform/external/rust/crates/codespan-reporting | androidbp,cargo | Bug: 156794058 |
| platform/external/rust/crates/combine | androidbp,cargo,rustfmt | combine An implementation of parser combinators fo |
| platform/external/rust/crates/command-fds | androidbp,cargo | command-fds A library for passing arbitrary file d |
| platform/external/rust/crates/config | androidbp,cargo | config-rs Layered configuration system for Rust ap |
| platform/external/rust/crates/configparser | androidbp,cargo | configparser This crate provides the Ini struct wh |
| platform/external/rust/crates/const-oid | androidbp,cargo | RustCrypto : Object Identifiers (OIDs) Const-frien |
| platform/external/rust/crates/const_fn | androidbp,cargo,rs_file | #[const_fn] An attribute for easy generation of co |
| platform/external/rust/crates/cortex-a | cargo | cortex-a Low level access to Cortex-A processors.  |
| platform/external/rust/crates/coset | androidbp,cargo | COSET This crate holds a set of Rust types for wor |
| platform/external/rust/crates/cov-mark | androidbp,cargo | cov-mark Verify that your tests exercise the condi |
| platform/external/rust/crates/crc32fast | androidbp,cargo,rs_file | crc32fast Fast, SIMD-accelerated CRC32 (IEEE) chec |
| platform/external/rust/crates/criterion | androidbp,cargo | Bug: 179317088 |
| platform/external/rust/crates/criterion-plot | androidbp,cargo | Bug: 179320179 |
| platform/external/rust/crates/critical-section | cargo | critical-section This project is developed and mai |
| platform/external/rust/crates/crossbeam-channel | androidbp,cargo | Crossbeam Channel This crate provides multi-produc |
| platform/external/rust/crates/crossbeam-deque | androidbp,cargo | Crossbeam Deque This crate provides work-stealing  |
| platform/external/rust/crates/crossbeam-epoch | androidbp,cargo | Crossbeam Epoch This crate provides epoch-based ga |
| platform/external/rust/crates/crossbeam-queue | androidbp,cargo | Crossbeam Queue This crate provides concurrent que |
| platform/external/rust/crates/crossbeam-utils | androidbp,cargo,rs_file | Crossbeam Utils This crate provides miscellaneous  |
| platform/external/rust/crates/csv | androidbp,cargo,rustfmt | csv A fast and flexible CSV reader and writer for  |
| platform/external/rust/crates/csv-core | androidbp,cargo | csv-core A fast CSV reader and write for use in a  |
| platform/external/rust/crates/darling | androidbp,cargo | Darling [ ] darling is a crate for proc macro auth |
| platform/external/rust/crates/darling_core | androidbp,cargo | Bug: 328419565 |
| platform/external/rust/crates/darling_macro | androidbp,cargo | Bug: 328420133 |
| platform/external/rust/crates/dashmap | androidbp,cargo | DashMap Blazingly fast concurrent map in Rust. Das |
| platform/external/rust/crates/data-encoding | androidbp,cargo | This library provides the following common encodin |
| platform/external/rust/crates/debug_tree | androidbp,cargo | Debug Tree This library allows you to build a tree |
| platform/external/rust/crates/der | androidbp,cargo | RustCrypto : ASN.1 DER Pure Rust embedded-friendly |
| platform/external/rust/crates/der-oid-macro | androidbp,cargo | Bug: 193830683 |
| platform/external/rust/crates/der-parser | androidbp,cargo | BER/DER Parser A parser for Basic Encoding Rules ( |
| platform/external/rust/crates/der_derive | androidbp,cargo | RustCrypto : DER Custom Derive Support Custom deri |
| platform/external/rust/crates/derive-getters | androidbp,cargo | Derive Getters Simple Getters derive macro for gen |
| platform/external/rust/crates/derive_arbitrary | androidbp,cargo | #[derive(Arbitrary)] This crate implements support |
| platform/external/rust/crates/displaydoc | androidbp,cargo | derive(Display) /// From<docs> This library provid |
| platform/external/rust/crates/document-features | androidbp,cargo,rs_file,rustfmt | Document your crate's feature flags This crate pro |
| platform/external/rust/crates/downcast | androidbp,cargo | downcast A trait (& utilities) for downcasting tra |
| platform/external/rust/crates/downcast-rs | androidbp,cargo | downcast-rs Rust enums are great for types where a |
| platform/external/rust/crates/drm | androidbp,cargo | drm-rs A safe interface to the Direct Rendering Ma |
| platform/external/rust/crates/drm-ffi | androidbp,cargo | Bug: 328179939 |
| platform/external/rust/crates/drm-fourcc | androidbp,cargo,rs_file | drm-fourcc Provides an enums representing every pi |
| platform/external/rust/crates/either | androidbp,cargo | Bug: 179100382 |
| platform/external/rust/crates/enum-as-inner | cargo | enum-as-inner A deriving proc-macro for generating |
| platform/external/rust/crates/enumn | androidbp,cargo | Convert number to enum This crate provides a deriv |
| platform/external/rust/crates/env_logger | androidbp,cargo | env_logger Implements a logger that can be configu |
| platform/external/rust/crates/epoll | androidbp,cargo,rustfmt | epoll Safe wrapper around the Linux kernel's epoll |
| platform/external/rust/crates/equivalent | androidbp,cargo | Equivalent Equivalent and Comparable are Rust trai |
| platform/external/rust/crates/errno | androidbp,cargo | errno Cross-platform interface to the errno variab |
| platform/external/rust/crates/etherparse | androidbp,cargo | etherparse A zero allocation supporting library fo |
| platform/external/rust/crates/fallible-iterator | androidbp,cargo | rust-fallible-iterator Documentation “Fallible” it |
| platform/external/rust/crates/fallible-streaming-iterator | androidbp,cargo | fallible-streaming-iterator Documentation Fallible |
| platform/external/rust/crates/fastrand | androidbp,cargo | fastrand A simple and fast random number generator |
| platform/external/rust/crates/fixedbitset | androidbp,cargo | fixedbitset A simple fixed size bitset container f |
| platform/external/rust/crates/flagset | androidbp,cargo | Welcome to FlagSet! FlagSet is a new, ergonomic ap |
| platform/external/rust/crates/flate2 | androidbp,cargo | flate2 A streaming compression/decompression libra |
| platform/external/rust/crates/fnv | androidbp,cargo,rs_file | rust-fnv An implementation of the Fowler–Noll–Vo h |
| platform/external/rust/crates/foreign-types | androidbp,cargo | foreign-types Documentation A framework for Rust w |
| platform/external/rust/crates/foreign-types-shared | androidbp,cargo | Bug: 230519341 |
| platform/external/rust/crates/form_urlencoded | androidbp,cargo | Bug: 175870104 |
| platform/external/rust/crates/fragile | androidbp,cargo | Fragile This library provides wrapper types that p |
| platform/external/rust/crates/fs-err | androidbp,cargo,rs_file | fs-err fs-err is a drop-in replacement for std::fs |
| platform/external/rust/crates/futures | androidbp,cargo | futures-rs is a library providing the foundations  |
| platform/external/rust/crates/futures-channel | androidbp,cargo | futures-channel Channels for asynchronous communic |
| platform/external/rust/crates/futures-core | androidbp,cargo | futures-core The core traits and types in for the  |
| platform/external/rust/crates/futures-executor | androidbp,cargo | futures-executor Executors for asynchronous tasks  |
| platform/external/rust/crates/futures-io | androidbp,cargo | futures-io The AsyncRead , AsyncWrite , AsyncSeek  |
| platform/external/rust/crates/futures-macro | androidbp,cargo | Bug: 152066863 |
| platform/external/rust/crates/futures-sink | androidbp,cargo | futures-sink The asynchronous Sink trait for the f |
| platform/external/rust/crates/futures-task | androidbp,cargo | futures-task Tools for working with tasks. Usage A |
| platform/external/rust/crates/futures-test | androidbp,cargo | futures-test Common utilities for testing componen |
| platform/external/rust/crates/futures-util | androidbp,cargo | futures-util Common utilities and extension traits |
| platform/external/rust/crates/fxhash | androidbp,cargo,rs_file | Fx Hash This hashing algorithm was extracted from  |
| platform/external/rust/crates/gbm | androidbp,cargo | Safe libgbm bindings for rust The Generic Buffer M |
| platform/external/rust/crates/gdbstub | androidbp,cargo,rustfmt | gdbstub An ergonomic, featureful, and easy-to-inte |
| platform/external/rust/crates/gdbstub_arch | androidbp,cargo | gdbstub_arch Community-contributed implementations |
| platform/external/rust/crates/getrandom | androidbp,cargo | getrandom A Rust library for retrieving random dat |
| platform/external/rust/crates/glam | androidbp,cargo | glam A simple and fast 3D math library for games a |
| platform/external/rust/crates/glob | androidbp,cargo | glob Support for matching file paths against Unix  |
| platform/external/rust/crates/googletest | androidbp,cargo | GoogleTest Rust This library brings the rich asser |
| platform/external/rust/crates/googletest_macro | androidbp,cargo | Procedural macros for GoogleTest Rust This crate i |
| platform/external/rust/crates/gpio-cdev | androidbp,cargo | gpio-cdev API Documentation rust-gpio-cdev is a Ru |
| platform/external/rust/crates/grpcio | androidbp,cargo | gRPC-rs gRPC-rs is a Rust wrapper of gRPC Core . g |
| platform/external/rust/crates/grpcio-compiler | androidbp,cargo | Bug: 172247654 |
| platform/external/rust/crates/grpcio-sys | androidbp,cargo,rs_file | Bug: 170765308 |
| platform/external/rust/crates/h2 | androidbp,cargo | H2 A Tokio aware, HTTP/2 client & server implement |
| platform/external/rust/crates/half | androidbp,cargo | f16 and bf16 floating point types for Rust This cr |
| platform/external/rust/crates/hashbrown | androidbp,cargo | hashbrown This crate is a Rust port of Google‘s hi |
| platform/external/rust/crates/hashlink | androidbp,cargo | hashlink -- HashMap-like containers that hold thei |
| platform/external/rust/crates/heck | androidbp,cargo | heck is a case conversion library This library exi |
| platform/external/rust/crates/hex | androidbp,cargo | hex Encoding and decoding data into/from hexadecim |
| platform/external/rust/crates/hickory-proto | cargo | Overview Hickory DNS Proto is the foundational DNS |
| platform/external/rust/crates/hound | androidbp,cargo | Hound A wav encoding and decoding library in Rust. |
| platform/external/rust/crates/http | androidbp,cargo | HTTP A general purpose library of common HTTP type |
| platform/external/rust/crates/http-body | androidbp,cargo | HTTP Body A trait representing asynchronous operat |
| platform/external/rust/crates/httparse | androidbp,cargo,rs_file | httparse A push parser for the HTTP 1.x protocol.  |
| platform/external/rust/crates/httpdate | androidbp,cargo | Date and time utils for HTTP. Multiple HTTP header |
| platform/external/rust/crates/hyper | androidbp,cargo | Bug: 342499482 |
| platform/external/rust/crates/hyper-timeout | androidbp,cargo | hyper-timeout A connect, read and write timeout aw |
| platform/external/rust/crates/ident_case | androidbp,cargo | Crate for manipulating case of identifiers in Rust |
| platform/external/rust/crates/idna | androidbp,cargo | Bug: 175870120 |
| platform/external/rust/crates/indexmap | androidbp,cargo,rs_file | indexmap A pure-Rust hash table which preserves (i |
| platform/external/rust/crates/inotify | androidbp,cargo | inotify-rs Idiomatic inotify wrapper for the Rust  |
| platform/external/rust/crates/inotify-sys | androidbp,cargo | inotify-sys Low-level inotify bindings for the Rus |
| platform/external/rust/crates/instant | androidbp,cargo | Instant If you call std::time::Instant::now() on a |
| platform/external/rust/crates/intrusive-collections | androidbp,cargo | intrusive-collections A Rust library for creating  |
| platform/external/rust/crates/ipnet | cargo | This module provides types and useful methods for  |
| platform/external/rust/crates/itertools | androidbp,cargo | Itertools Extra iterator adaptors, functions and m |
| platform/external/rust/crates/itoa | androidbp,cargo | itoa This crate provides a fast conversion of inte |
| platform/external/rust/crates/jni | androidbp,cargo | JNI Bindings for Rust This project provides comple |
| platform/external/rust/crates/jni-sys | androidbp,cargo | jni-sys Documentation Rust definitions correspondi |
| platform/external/rust/crates/kernlog | androidbp,cargo | Kernel logger for Rust Logger implementation for l |
| platform/external/rust/crates/lazy_static | androidbp,cargo | lazy-static.rs A macro for declaring lazily evalua |
| platform/external/rust/crates/lazycell | androidbp,cargo | lazycell Rust library providing a lazily filled Ce |
| platform/external/rust/crates/libbpf-rs | androidbp,cargo,rs_file | libbpf-rs Idiomatic Rust wrapper around libbpf . C |
| platform/external/rust/crates/libbpf-sys | androidbp,cargo,rs_file | libbpf-sys Rust bindings to libbpf from the Linux  |
| platform/external/rust/crates/libc | androidbp,cargo,rs_file,rustfmt | libc - Raw FFI bindings to platforms' system libra |
| platform/external/rust/crates/libfuzzer-sys | androidbp,cargo,rs_file | The libfuzzer-sys Crate Barebones wrapper around L |
| platform/external/rust/crates/libloading | androidbp,cargo | Bug: 154099606 |
| platform/external/rust/crates/libm | androidbp,cargo,rs_file | libm A port of MUSL 's libm to Rust. Goals The sho |
| platform/external/rust/crates/libsqlite3-sys | androidbp,cargo,rs_file | Rusqlite Rusqlite is an ergonomic wrapper for usin |
| platform/external/rust/crates/libtest-mimic | androidbp,cargo | libtest-mimic Write your own test harness that loo |
| platform/external/rust/crates/libusb1-sys | androidbp,cargo,rs_file | Libusb Rust Bindings The libusb1-sys crate provide |
| platform/external/rust/crates/libz-sys | androidbp,cargo,rs_file | libz-sys A common library for linking libz to rust |
| platform/external/rust/crates/linked-hash-map | androidbp,cargo | WARNING: THIS PROJECT IS IN MAINTENANCE MODE, DUE  |
| platform/external/rust/crates/linkme | androidbp,cargo | Linkme: safe cross-platform linker shenanigans Com |
| platform/external/rust/crates/linkme-impl | androidbp,cargo | Bug: 285065716 |
| platform/external/rust/crates/litrs | androidbp,cargo | litrs : parsing and inspecting Rust literals litrs |
| platform/external/rust/crates/lock_api | androidbp,cargo,rs_file | Bug: 170749427 |
| platform/external/rust/crates/log | androidbp,cargo,rs_file | log A Rust library providing a lightweight logging |
| platform/external/rust/crates/lru-cache | androidbp,cargo | WARNING: THIS PROJECT IS IN MAINTENANCE MODE, DUE  |
| platform/external/rust/crates/lz4_flex | androidbp,cargo | lz4_flex Fastest LZ4 implementation in Rust. Origi |
| platform/external/rust/crates/macaddr | androidbp,cargo,rustfmt | macaddr MAC address types for Rust This crate prov |
| platform/external/rust/crates/managed | androidbp,cargo | Managed managed is a library that provides a way t |
| platform/external/rust/crates/maplit | androidbp,cargo | Bug: 374957872 |
| platform/external/rust/crates/matches | androidbp,cargo,rs_file | Bug: 175869252 |
| platform/external/rust/crates/matchit | androidbp,cargo | matchit A high performance, zero-copy URL router.  |
| platform/external/rust/crates/maybe-async | androidbp,cargo | maybe-async Why bother writing similar code twice  |
| platform/external/rust/crates/memchr | androidbp,cargo,rustfmt | memchr This library provides heavily optimized rou |
| platform/external/rust/crates/memmap2 | androidbp,cargo | memmap2 A Rust library for cross-platform memory m |
| platform/external/rust/crates/memoffset | androidbp,cargo,rs_file | memoffset C-Like offset_of functionality for Rust  |
| platform/external/rust/crates/merge | androidbp,cargo | merge-rs The merge crate provides the Merge trait  |
| platform/external/rust/crates/merge_derive | androidbp,cargo | merge-derive-rs This crate provides a derive macro |
| platform/external/rust/crates/miette | androidbp,cargo,rustfmt | miette You run miette? You run her code like the s |
| platform/external/rust/crates/miette-derive | androidbp,cargo | Bug: 288514263 |
| platform/external/rust/crates/mime | androidbp,cargo | mime Support MIME (Media Types) as strong types in |
| platform/external/rust/crates/minimal-lexical | androidbp,cargo,rustfmt | minimal-lexical This is a minimal version of rust- |
| platform/external/rust/crates/mio | androidbp,cargo | Mio – Metal I/O Mio is a fast, low-level I/O libra |
| platform/external/rust/crates/mls-rs | androidbp,cargo | mls-rs An implementation of the IETF Messaging Lay |
| platform/external/rust/crates/mls-rs-codec | androidbp,cargo | Bug: 328421610 |
| platform/external/rust/crates/mls-rs-codec-derive | androidbp,cargo | Bug: 328421132 |
| platform/external/rust/crates/mls-rs-core | androidbp,cargo | Bug: 328421156 |
| platform/external/rust/crates/mls-rs-crypto-traits | androidbp,cargo | Bug: 335422504 |
| platform/external/rust/crates/mls-rs-uniffi | cargo | Bug: 336992562 |
| platform/external/rust/crates/mockall | androidbp,cargo | Mockall A powerful mock object library for Rust. O |
| platform/external/rust/crates/mockall_derive | androidbp,cargo | Mockall_derive This crate should never be used dir |
| platform/external/rust/crates/moveit | androidbp,cargo,rustfmt | moveit A library for safe, in-place construction o |
| platform/external/rust/crates/named-lock | androidbp,cargo,rustfmt | named-lock This crate provides a simple and cross- |
| platform/external/rust/crates/nix | androidbp,cargo,rs_file | Rust bindings to *nix APIs Documentation (Releases |
| platform/external/rust/crates/no-panic | androidbp,cargo | #[no_panic] A Rust attribute macro to require that |
| platform/external/rust/crates/nom | androidbp,cargo | nom, eating data byte by byte nom is a parser comb |
| platform/external/rust/crates/num-bigint | androidbp,cargo,rs_file | num-bigint Big integer types for Rust, BigInt and  |
| platform/external/rust/crates/num-complex | androidbp,cargo | num-complex Complex numbers for Rust. Usage Add th |
| platform/external/rust/crates/num-derive | androidbp,cargo | num-derive Procedural macros to derive numeric tra |
| platform/external/rust/crates/num-integer | androidbp,cargo,rs_file | num-integer Integer trait and functions for Rust.  |
| platform/external/rust/crates/num-traits | androidbp,cargo,rs_file | num-traits Numeric traits for generic mathematics  |
| platform/external/rust/crates/num_cpus | androidbp,cargo | num_cpus Documentation CHANGELOG Count the number  |
| platform/external/rust/crates/num_enum | androidbp,cargo | num_enum Procedural macros to make inter-operation |
| platform/external/rust/crates/num_enum_derive | androidbp,cargo | num_enum Procedural macros to make inter-operation |
| platform/external/rust/crates/octets | androidbp,cargo | Bug: 246974262 |
| platform/external/rust/crates/oid-registry | androidbp,cargo,rs_file | OID Registry This crate is a helper crate, contain |
| platform/external/rust/crates/once_cell | androidbp,cargo | Overview once_cell provides two new cell-like type |
| platform/external/rust/crates/oneshot-uniffi | androidbp,cargo | oneshot Oneshot spsc (single producer, single cons |
| platform/external/rust/crates/oorandom | androidbp,cargo | oorandom What is this? oorandom is a minimalistic  |
| platform/external/rust/crates/openssl | androidbp,cargo,rs_file | rust-openssl OpenSSL bindings for the Rust program |
| platform/external/rust/crates/openssl-macros | androidbp,cargo | Bug: 262438682 |
| platform/external/rust/crates/os_str_bytes | androidbp,cargo | OsStr Bytes This crate allows interacting with the |
| platform/external/rust/crates/p9 | androidbp,cargo | p9 - Server implementation of the 9p file system p |
| platform/external/rust/crates/p9_wire_format_derive | androidbp,cargo | p9 - Server implementation of the 9p file system p |
| platform/external/rust/crates/parking_lot | androidbp,cargo | parking_lot Documentation (synchronization primiti |
| platform/external/rust/crates/parking_lot_core | androidbp,cargo,rs_file | Bug: 170684118 |
| platform/external/rust/crates/paste | androidbp,cargo,rs_file | Macros for all your token pasting needs The nightl |
| platform/external/rust/crates/paste-impl | androidbp,cargo | Bug: 152401996 |
| platform/external/rust/crates/pathdiff | androidbp,cargo | Bug: 288516638 |
| platform/external/rust/crates/pdl-compiler | androidbp,cargo | Packet Description Language (PDL) PDL is a domain  |
| platform/external/rust/crates/pdl-runtime | androidbp,cargo | Packet Description Language (PDL) PDL is a domain  |
| platform/external/rust/crates/peeking_take_while | androidbp,cargo | peeking_take_while Provides the peeking_take_while |
| platform/external/rust/crates/percent-encoding | androidbp,cargo | Bug: 175870079 |
| platform/external/rust/crates/percore | androidbp,cargo | percore Safe per-CPU core mutable state on no_std  |
| platform/external/rust/crates/pest | androidbp,cargo | Bug: 218419981 |
| platform/external/rust/crates/pest_derive | androidbp,cargo | Bug: 218410551 |
| platform/external/rust/crates/pest_generator | androidbp,cargo | Bug: 218416559 |
| platform/external/rust/crates/pest_meta | androidbp,cargo | Bug: 218414352 |
| platform/external/rust/crates/petgraph | androidbp,cargo | petgraph Graph data structure library. Please read |
| platform/external/rust/crates/pin-project | androidbp,cargo | pin-project A crate for safe and ergonomic pin-pro |
| platform/external/rust/crates/pin-project-internal | androidbp,cargo | Bug: 156522606 |
| platform/external/rust/crates/pin-project-lite | androidbp,cargo | pin-project-lite A lightweight version of pin-proj |
| platform/external/rust/crates/pin-utils | androidbp,cargo | pin-utils Utilities for pinning Documentation Usag |
| platform/external/rust/crates/pkcs1 | androidbp,cargo | RustCrypto : PKCS#1 (RSA) Pure Rust implementation |
| platform/external/rust/crates/pkcs8 | androidbp,cargo | RustCrypto : PKCS#8 (Private Keys) Pure Rust imple |
| platform/external/rust/crates/plotters | androidbp,cargo | ../README.md |
| platform/external/rust/crates/plotters-backend | androidbp,cargo | plotters-backend - The base crate for implementing |
| platform/external/rust/crates/plotters-svg | androidbp,cargo | plotters-svg - The SVG backend for Plotters This i |
| platform/external/rust/crates/poll_token_derive | androidbp,cargo,rs_file | Bug: 369747276 |
| platform/external/rust/crates/portable-atomic | cargo,rs_file | portable-atomic Portable atomic types including su |
| platform/external/rust/crates/ppv-lite86 | androidbp,cargo | Bug: 159928773 |
| platform/external/rust/crates/predicates | androidbp,cargo | predicates-rs An implementation of boolean-valued  |
| platform/external/rust/crates/predicates-core | androidbp,cargo | predicates-core Traits for boolean-valued predicat |
| platform/external/rust/crates/predicates-tree | androidbp,cargo | predicates-tree Render boolean-valued predicate fu |
| platform/external/rust/crates/prettyplease | androidbp,cargo,rs_file | prettyplease::unparse A minimal syn syntax tree pr |
| platform/external/rust/crates/proc-macro-error | androidbp,cargo,rs_file | Makes error reporting in procedural macros nice an |
| platform/external/rust/crates/proc-macro-error-attr | androidbp,cargo,rs_file | Bug: 156527773 |
| platform/external/rust/crates/proc-macro-hack | androidbp,cargo,rs_file | Procedural macros in expression position Since Rus |
| platform/external/rust/crates/proc-macro-nested | androidbp,cargo,rs_file | Bug: 152624124 |
| platform/external/rust/crates/proc-macro2 | androidbp,cargo,rs_file | proc-macro2 A wrapper around the procedural macro  |
| platform/external/rust/crates/protobuf | androidbp,cargo,rs_file | Library to read and write protocol buffers data Fe |
| platform/external/rust/crates/protobuf-codegen | androidbp,cargo | Protobuf code generator for protobuf crate This cr |
| platform/external/rust/crates/protobuf-json-mapping | androidbp,cargo | JSON printer and parser which tries to follow prot |
| platform/external/rust/crates/protobuf-parse | androidbp,cargo | Parse .proto files Parse .proto file definitions,  |
| platform/external/rust/crates/protobuf-support | androidbp,cargo | Supporting code for protobuf crates Code in this c |
| platform/external/rust/crates/psci | androidbp,cargo | SMCCC and PSCI functions for bare-metal Rust on aa |
| platform/external/rust/crates/ptr_meta | androidbp,cargo | ptr_meta ptr_meta A radioactive stabilization of t |
| platform/external/rust/crates/ptr_meta_derive | androidbp,cargo | Bug: 377556466 |
| platform/external/rust/crates/quiche | androidbp,cargo | quiche is an implementation of the QUIC transport  |
| platform/external/rust/crates/quickcheck | androidbp,cargo,rustfmt | quickcheck QuickCheck is a way to do property base |
| platform/external/rust/crates/quote | androidbp,cargo | Rust Quasi-Quoting This crate provides the quote!  |
| platform/external/rust/crates/rand | androidbp,cargo | Rand A Rust library for random number generation,  |
| platform/external/rust/crates/rand_chacha | androidbp,cargo | rand_chacha A cryptographically secure random numb |
| platform/external/rust/crates/rand_core | androidbp,cargo | rand_core Core traits and error types of the rand  |
| platform/external/rust/crates/rand_xorshift | androidbp,cargo | rand_xorshift Implements the Xorshift random numbe |
| platform/external/rust/crates/rayon | androidbp,cargo | Rayon Rayon is a data-parallelism library for Rust |
| platform/external/rust/crates/rayon-core | androidbp,cargo,rs_file | Rayon-core represents the “core, stable” APIs of R |
| platform/external/rust/crates/regex | androidbp,cargo,rustfmt | regex A Rust library for parsing, compiling, and e |
| platform/external/rust/crates/regex-automata | androidbp,cargo,rustfmt | regex-automata A low level regular expression libr |
| platform/external/rust/crates/regex-syntax | androidbp,cargo | regex-syntax This crate provides a robust regular  |
| platform/external/rust/crates/remain | androidbp,cargo | Remain sorted This crate provides an attribute mac |
| platform/external/rust/crates/remove_dir_all | androidbp,cargo | remove_dir_all Description Reliable and fast direc |
| platform/external/rust/crates/ring | androidbp,cargo,rs_file | Bug: 174788910 |
| platform/external/rust/crates/rusb | androidbp,cargo,rs_file | Rusb This crate provides a safe wrapper around the |
| platform/external/rust/crates/rusqlite | androidbp,cargo | Rusqlite Rusqlite is an ergonomic wrapper for usin |
| platform/external/rust/crates/rust-stemmers | cargo | Rust Stemmers This crate implements some stemmer a |
| platform/external/rust/crates/rustc-demangle | androidbp,cargo | rustc-demangle Demangling for Rust symbols, writte |
| platform/external/rust/crates/rustc-demangle-capi | androidbp,cargo | Bug: 183698465 |
| platform/external/rust/crates/rustc-hash | androidbp,cargo | rustc-hash A speedy hash algorithm used within rus |
| platform/external/rust/crates/rusticata-macros | androidbp,cargo | rusticata-macros Rusticata-macros Helper macros fo |
| platform/external/rust/crates/rustix | androidbp,cargo,rs_file | A Bytecode Alliance project rustix provides effici |
| platform/external/rust/crates/rustversion | androidbp,cargo | Compiler version cfg This crate provides macros fo |
| platform/external/rust/crates/ryu | androidbp,cargo | Ryū Pure Rust implementation of Ryū, an algorithm  |
| platform/external/rust/crates/same-file | androidbp,cargo,rustfmt | same-file A safe and cross platform crate to deter |
| platform/external/rust/crates/scopeguard | androidbp,cargo | scopeguard Rust crate for a convenient RAII scope  |
| platform/external/rust/crates/sec1 | androidbp,cargo | RustCrypto : SEC1 Elliptic Curve Cryptography Form |
| platform/external/rust/crates/semver | androidbp,cargo,rs_file | semver A parser and evaluator for Cargo's flavor o |
| platform/external/rust/crates/serde | androidbp,cargo,rs_file | Serde Serde is a framework for ser ializing and de |
| platform/external/rust/crates/serde-xml-rs | androidbp,cargo,rustfmt | serde-xml-rs xml-rs based deserializer for Serde ( |
| platform/external/rust/crates/serde_cbor | androidbp,cargo | Serde CBOR PROJECT IS ARCHIVED After almost 6 year |
| platform/external/rust/crates/serde_derive | androidbp,cargo,rs_file | Serde Serde is a framework for ser ializing and de |
| platform/external/rust/crates/serde_json | androidbp,cargo,rs_file | Serde JSON Serde is a framework for ser ializing a |
| platform/external/rust/crates/serde_spanned | androidbp,cargo | serde_spanned A serde -compatible spanned Value Th |
| platform/external/rust/crates/serde_test | androidbp,cargo | serde_test This crate provides a convenient concis |
| platform/external/rust/crates/serde_yaml | androidbp,cargo | Serde YAML This crate is a Rust library for using  |
| platform/external/rust/crates/sharded-slab | androidbp,cargo | sharded-slab A lock-free concurrent slab. Slabs pr |
| platform/external/rust/crates/shared_child | androidbp,cargo | shared_child.rs A library for awaiting and killing |
| platform/external/rust/crates/shared_library | androidbp,cargo | Bug: 190426302 |
| platform/external/rust/crates/shlex | androidbp,cargo | Same idea as (but implementation not directly base |
| platform/external/rust/crates/siphasher | androidbp,cargo | SipHash implementation for Rust This crates implem |
| platform/external/rust/crates/slab | androidbp,cargo,rs_file | Slab Pre-allocated storage for a uniform data type |
| platform/external/rust/crates/smallvec | androidbp,cargo | rust-smallvec Documentation Release notes “Small v |
| platform/external/rust/crates/smccc | androidbp,cargo | SMCCC and PSCI functions for bare-metal Rust on aa |
| platform/external/rust/crates/smoltcp | cargo,rs_file | smoltcp smoltcp is a standalone, event-driven TCP/ |
| platform/external/rust/crates/socket2 | androidbp,cargo | Socket2 Socket2 is a crate that provides utilities |
| platform/external/rust/crates/spin | androidbp,cargo | spin-rs Spin-based synchronization primitives. Thi |
| platform/external/rust/crates/spki | androidbp,cargo | RustCrypto : X.509 Subject Public Key Info (SPKI)  |
| platform/external/rust/crates/standback | androidbp,cargo,rs_file | Standback Documentation Standback exists to allow  |
| platform/external/rust/crates/static_assertions | androidbp,cargo | Compile-time assertions for Rust, brought to you b |
| platform/external/rust/crates/strsim | androidbp,cargo | strsim-rs Rust implementations of string similarit |
| platform/external/rust/crates/structopt | androidbp,cargo | StructOpt Parse command line arguments by defining |
| platform/external/rust/crates/structopt-derive | androidbp,cargo | Bug: 156794060 |
| platform/external/rust/crates/strum | androidbp,cargo | Bug: 319324143 |
| platform/external/rust/crates/strum_macros | androidbp,cargo | Strum Strum is a set of macros and traits for work |
| platform/external/rust/crates/syn | androidbp,cargo | Parser for Rust source code Syn is a parsing libra |
| platform/external/rust/crates/syn-mid | androidbp,cargo | syn-mid Providing the features between “full” and  |
| platform/external/rust/crates/sync_wrapper | androidbp,cargo | SyncWrapper A mutual exclusion primitive that reli |
| platform/external/rust/crates/synstructure | androidbp,cargo | synstructure NOTE: What follows is an exerpt from  |
| platform/external/rust/crates/tempfile | androidbp,cargo | tempfile A secure, cross-platform, temporary file  |
| platform/external/rust/crates/termcolor | androidbp,cargo,rustfmt | termcolor A simple cross platform library for writ |
| platform/external/rust/crates/terminal-size | androidbp,cargo | terminal-size Documention Rust library to getting  |
| platform/external/rust/crates/termtree | androidbp,cargo | termtree Visualize tree-like data on the command-l |
| platform/external/rust/crates/textwrap | androidbp,cargo,rustfmt | Textwrap Textwrap is a library for wrapping and in |
| platform/external/rust/crates/thiserror | androidbp,cargo,rs_file | derive(Error) This library provides a convenient d |
| platform/external/rust/crates/thiserror-impl | androidbp,cargo | Bug: 157243935 |
| platform/external/rust/crates/thread_local | androidbp,cargo | thread_local This library provides the ThreadLocal |
| platform/external/rust/crates/threadpool | androidbp,cargo | Bug: 279644798 |
| platform/external/rust/crates/tikv-jemalloc-sys | androidbp,cargo | jemalloc-sys - Rust bindings to the jemalloc C lib |
| platform/external/rust/crates/tikv-jemallocator | androidbp,cargo | tikv-jemallocator This project is the successor of |
| platform/external/rust/crates/time | androidbp,cargo | time Utilities for working with time-related funct |
| platform/external/rust/crates/time-macros | cargo | Bug: 171359410 |
| platform/external/rust/crates/time-macros-impl | androidbp,cargo | Bug: 171359136 |
| platform/external/rust/crates/tinyjson | cargo | tinyjson tinyjson is a library to parse/generate J |
| platform/external/rust/crates/tinytemplate | androidbp,cargo | Bug: 181073064 |
| platform/external/rust/crates/tinyvec | androidbp,cargo,rustfmt | tinyvec A 100% safe crate of vec-like types. #![fo |
| platform/external/rust/crates/tinyvec_macros | androidbp,cargo | Bug: 175870075 |
| platform/external/rust/crates/tock-registers | androidbp,cargo | Tock Register Interface This crate provides an int |
| platform/external/rust/crates/tokio | androidbp,cargo | Tokio A runtime for writing reliable, asynchronous |
| platform/external/rust/crates/tokio-io-timeout | androidbp,cargo | tokio-io-timeout Documentation Tokio wrappers whic |
| platform/external/rust/crates/tokio-macros | androidbp,cargo | Tokio Macros Procedural macros for use with Tokio  |
| platform/external/rust/crates/tokio-openssl | androidbp,cargo,rs_file | tokio-openssl An implementation of SSL streams for |
| platform/external/rust/crates/tokio-stream | androidbp,cargo | Bug: 178378678 |
| platform/external/rust/crates/tokio-test | androidbp,cargo | tokio-test Tokio and Futures based testing utiliti |
| platform/external/rust/crates/tokio-util | androidbp,cargo | tokio-util Utilities for working with Tokio. Licen |
| platform/external/rust/crates/toml | androidbp,cargo | toml A serde -compatible TOML decoder and encoder  |
| platform/external/rust/crates/toml_datetime | androidbp,cargo | toml_datetime License This project is licensed und |
| platform/external/rust/crates/toml_edit | androidbp,cargo | toml_edit This crate allows you to parse and modif |
| platform/external/rust/crates/tonic | androidbp,cargo | A rust implementation of gRPC , a high performance |
| platform/external/rust/crates/tower | androidbp,cargo | Tower Tower is a library of modular and reusable c |
| platform/external/rust/crates/tower-layer | androidbp,cargo | Tower Layer Decorates a Tower Service , transformi |
| platform/external/rust/crates/tower-service | androidbp,cargo | Tower Service The foundational Service trait that  |
| platform/external/rust/crates/tracing | androidbp,cargo | tracing Application-level tracing for Rust. Docume |
| platform/external/rust/crates/tracing-attributes | androidbp,cargo | tracing-attributes Macro attributes for applicatio |
| platform/external/rust/crates/tracing-core | androidbp,cargo | tracing-core Core primitives for application-level |
| platform/external/rust/crates/tracing-subscriber | androidbp,cargo | tracing-subscriber Utilities for implementing and  |
| platform/external/rust/crates/try-lock | androidbp,cargo | TryLock Crates.io Docs A light-weight lock guarded |
| platform/external/rust/crates/tungstenite | androidbp,cargo | Tungstenite Lightweight stream-based WebSocket imp |
| platform/external/rust/crates/twox-hash | androidbp,cargo | TwoX-Hash A Rust implementation of the XXHash algo |
| platform/external/rust/crates/ucd-trie | androidbp,cargo | ucd-trie A library that provides compressed trie s |
| platform/external/rust/crates/ucs2 | androidbp,cargo | ucs2-rs UCS-2 handling for Rust. Note that UCS-2 i |
| platform/external/rust/crates/uefi | androidbp,cargo | uefi Rusty wrapper for the Unified Extensible Firm |
| platform/external/rust/crates/uefi-macros | androidbp,cargo | uefi-macros This crate provides procedural macros  |
| platform/external/rust/crates/uefi-raw | androidbp,cargo | uefi-raw This crate contains raw UEFI types that c |
| platform/external/rust/crates/uguid | androidbp,cargo | uguid no_std library providing a GUID (Globally Un |
| platform/external/rust/crates/unicode-bidi | androidbp,cargo | unicode-bidi This crate implements the Unicode Bid |
| platform/external/rust/crates/unicode-ident | androidbp,cargo | Unicode ident Implementation of Unicode Standard A |
| platform/external/rust/crates/unicode-normalization | androidbp,cargo | unicode-normalization Unicode character compositio |
| platform/external/rust/crates/unicode-segmentation | androidbp,cargo | Iterators which split strings on Grapheme Cluster  |
| platform/external/rust/crates/unicode-width | androidbp,cargo | unicode-width Determine displayed width of char an |
| platform/external/rust/crates/unicode-xid | androidbp,cargo | unicode-xid Determine if a char is a valid identif |
| platform/external/rust/crates/uniffi | androidbp,cargo | UniFFI - a multi-language bindings generator for R |
| platform/external/rust/crates/uniffi_checksum_derive | androidbp,cargo | UniFFI - a multi-language bindings generator for R |
| platform/external/rust/crates/uniffi_core | androidbp,cargo | UniFFI - a multi-language bindings generator for R |
| platform/external/rust/crates/uniffi_macros | androidbp,cargo | UniFFI - a multi-language bindings generator for R |
| platform/external/rust/crates/uniffi_meta | androidbp,cargo | UniFFI - a multi-language bindings generator for R |
| platform/external/rust/crates/unsafe-libyaml | androidbp,cargo | unsafe-libyaml This library is libyaml translated  |
| platform/external/rust/crates/untrusted | androidbp,cargo,rustfmt | THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHORS D |
| platform/external/rust/crates/url | androidbp,cargo | rust-url URL library for Rust, based on the URL St |
| platform/external/rust/crates/userfaultfd | androidbp,cargo | Userfaultfd-rs Rust bindings for Linux's userfault |
| platform/external/rust/crates/userfaultfd-sys | androidbp,cargo,rs_file | Bug: 259594956 |
| platform/external/rust/crates/utf-8 | androidbp,cargo | rust-utf8 Incremental, zero-copy UTF-8 decoding fo |
| platform/external/rust/crates/uuid | androidbp,cargo | uuid Here's an example of a UUID: 67e55044 - 10b1  |
| platform/external/rust/crates/v4l2r | androidbp,cargo | Rust bindings for V4L2 This is a work-in-progress  |
| platform/external/rust/crates/vhost | androidbp,cargo | vHost A pure rust library for vDPA, vhost and vhos |
| platform/external/rust/crates/vhost-device-vsock | androidbp,cargo | vhost-device-vsock Design The crate introduces a v |
| platform/external/rust/crates/vhost-user-backend | androidbp,cargo | vhost-user-backend Design The vhost-user-backend c |
| platform/external/rust/crates/virtio-bindings | androidbp,cargo | virtio-bindings Rust FFI bindings to virtio genera |
| platform/external/rust/crates/virtio-drivers | androidbp,cargo | VirtIO-drivers-rs VirtIO guest drivers in Rust. Fo |
| platform/external/rust/crates/virtio-queue | androidbp,cargo | virtio-queue The virtio-queue crate provides a vir |
| platform/external/rust/crates/virtio-vsock | androidbp,cargo | virtio-vsock The virtio-vsock crate provides abstr |
| platform/external/rust/crates/vm-memory | androidbp,cargo | vm-memory Design In a typical Virtual Machine Moni |
| platform/external/rust/crates/vmm-sys-util | androidbp,cargo | vmm-sys-util This crate is a collection of modules |
| platform/external/rust/crates/vsock | androidbp,cargo | vsock-rs Virtio socket support for Rust. Implement |
| platform/external/rust/crates/vsprintf | androidbp,cargo,rs_file | vsprintf Convert a format string and vararg list t |
| platform/external/rust/crates/vulkano | androidbp,cargo,rs_file | Vulkano Vulkano is a Rust wrapper around the Vulka |
| platform/external/rust/crates/walkdir | androidbp,cargo,rustfmt | walkdir A cross platform Rust library for efficien |
| platform/external/rust/crates/want | androidbp,cargo | Want Crates.io Docs A Future s channel-like utilit |
| platform/external/rust/crates/weak-table | androidbp,cargo | weak-table: weak hash maps and sets for Rust This  |
| platform/external/rust/crates/webpki | androidbp,cargo | THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHORS D |
| platform/external/rust/crates/which | androidbp,cargo | which A Rust equivalent of Unix command “which”. L |
| platform/external/rust/crates/winnow | androidbp,cargo | winnow, making parsing a breeze About Build up a p |
| platform/external/rust/crates/x509-cert | androidbp,cargo | RustCrypto : X.509 Certificates Pure Rust implemen |
| platform/external/rust/crates/x509-parser | androidbp,cargo | X.509 Parser A X.509 v3 ( RFC5280 ) parser, implem |
| platform/external/rust/crates/xml-rs | androidbp,cargo | xml-rs, an XML library for Rust Documentation xml- |
| platform/external/rust/crates/yaml-rust | androidbp,cargo | yaml-rust The missing YAML 1.2 implementation for  |
| platform/external/rust/crates/zerocopy | androidbp,cargo,rustfmt | zerocopy Want to help improve zerocopy? Fill out o |
| platform/external/rust/crates/zerocopy-derive | androidbp,cargo | Bug: 262009284 |
| platform/external/rust/crates/zeroize | androidbp,cargo | RustCrypto : zeroize Securely zero memory (a.k.a.  |
| platform/external/rust/crates/zeroize_derive | androidbp,cargo | RustCrypto : zeroize_derive Custom derive support  |
| platform/external/rust/crates/zip | androidbp,cargo | zip-rs Documentation Info A zip library for rust w |
| platform/external/rust/crates/zune-inflate | cargo | zune-inflate This crate features an optimized infl |
| platform/external/rust/cros-libva | androidbp,cargo | Libva Rust Wrapper This crate provides lightweight |
| platform/external/rust/cxx | androidbp,cargo,rs_file | CXX — safe FFI between Rust and C++ This library p |
| platform/external/rust/pica | androidbp,cargo,rs_file | Pica Pica is a virtual UWB Controller implementing |
| platform/external/skia | androidbp,cargo | - |
| platform/external/toolchain-utils | rust_dir | toolchain-utils Various utilities used by the Chro |
| platform/external/uwb | androidbp,rustfmt | Bug: 237676695 |
| platform/external/vboot_reference | androidbp,rust_dir | - |
| platform/frameworks/minikin | androidbp,rust_dir | - |
| platform/frameworks/native | androidbp,rustfmt | - |
| platform/packages/modules/Bluetooth | androidbp,cargo,rustfmt | Fluoride Bluetooth stack Building and running on A |
| platform/packages/modules/DnsResolver | androidbp,rustfmt | Logging This code uses LOG(X) for logging. Log lev |
| platform/packages/modules/SdkExtensions | androidbp,rustfmt | SdkExtensions module SdkExtensions module is respo |
| platform/packages/modules/Uwb | androidbp,rustfmt | Bug: 189143511 |
| platform/packages/modules/Virtualization | androidbp,rustfmt | Android Virtualization Framework (AVF) Android Vir |
| platform/system/apex | androidbp,rustfmt | Bug: 112515528 |
| platform/system/authgraph | androidbp,cargo,rustfmt | Bug: 293191657 |
| platform/system/bpf | androidbp,rustfmt | Bug: 117234388 |
| platform/system/core | androidbp,rustfmt | minimal bootable environment |
| platform/system/cros-codecs | androidbp,cargo,rustfmt | Cros-codecs A lightweight, simple, low-dependency, |
| platform/system/extras | rustfmt | debugging/inspection tools |
| platform/system/keymint | androidbp,cargo,rustfmt | KeyMint Rust Reference Implementation This reposit |
| platform/system/libfmq | androidbp,rs_file | - |
| platform/system/librustutils | androidbp,rs_file | Bug: 195061451 |
| platform/system/logging | rust_dir | Bug: 168791309 |
| platform/system/memory/mmd | androidbp,rustfmt | mmd TBD Apply rustfmt Before upload your changes,  |
| platform/system/secretkeeper | androidbp,cargo,rustfmt | Secretkeeper Secretkeeper provides secure storage  |
| platform/system/secure_element | rustfmt | Bug: 397456726 |
| platform/system/security | androidbp,rustfmt | - |
| platform/system/see/authmgr | androidbp,rustfmt | Bug: 350548969 |
| platform/system/tools/aidl | androidbp,rustfmt | Documentation for this project is currently mainta |
| platform/system/tools/mkbootimg | androidbp,rust_dir | Bug: 133171083 |
| platform/tools/netsim | androidbp,rust_dir | netsim - a network simulation tool for multi-devic |
| platform/tools/security | rustfmt | Bug: 77098416 |
| tee/optee/ta/keymint | cargo,rustfmt | KeyMint reference implementation for OP-TEE This r |
| toolchain/cargo-deny | cargo | ❌ cargo-deny Cargo plugin for linting your depende |
| toolchain/cargo-vet | cargo | cargo-vet The cargo vet subcommand is a tool to he |
| toolchain/rustc | cargo | Website / Getting started / Learn / Documentation  |
| toolchain/sccache | cargo | sccache - Shared Compilation Cache sccache is a cc |
| trusty/app/authmgr | androidbp,rustfmt | Bug: 371226688 |
| trusty/app/keymint | androidbp,rs_file,rustfmt | Bug: 223458328 |
| trusty/app/sample | androidbp,rust_dir,rustfmt | - |
| trusty/app/secretkeeper | androidbp,rs_file,rustfmt | Bug: 310885032 |
| trusty/app/storage | androidbp,rustfmt | Secure storage service The secure storage service  |
| trusty/host/aidl | androidbp,rustfmt | Documentation for this project is currently mainta |
| trusty/host/common | rustfmt | Bug: 234928363 |
| trusty/lib | androidbp,rustfmt | - |
| trusty/lk/common | androidbp,rustfmt | LK The LK embedded kernel. An SMP-aware kernel des |
| trusty/lk/trusty | androidbp,rustfmt | - |
| trusty/user/desktop | androidbp,rustfmt | Bug: 361072469 |

- 仅有 Android.bp（无法单独判断语言）仓库数：892

## 3. 各前缀下的重点仓库
### platform（2111 个 ok）
- **abi/cpp**（1）：-
- **art**（1）：-
- **bbuildbot_config**（1）：This repository exists to configure cbuildbot based bruteus 
- **bionic**（1）：bionic maintainer overview bionic is Android's C library, ma
- **bootable/diskinstaller**（1）：-
- **bootable/libbootloader**（1）：Bug: 178600786
- **bootable/recovery**（1）：The Recovery Image Quick turn-around testing Devices using r
- **build**（1）：Android Make Build System This is the Makefile-based portion
- **build/bazel**（1）：Bazel The code in this directory is experimental. Bazel supp
- **build/bazel_common_rules**（1）：Bazel Common Rules This directory contains common Bazel rule
- **build/blueprint**（1）：Blueprint Build System Blueprint is part of Soong. For more 
- **build/kati**（1）：kati kati is an experimental GNU make clone. The main goal o
- **build/orchestrator**（1）：Bug: 240497793
- **build/pesto**（1）：Bug: 184970112
- **build/release**（1）：Bug: 282233606
- **build/soong**（1）：Soong Soong is one of the build systems used in Android. The
- **compatibility/cdd**（1）：See instructions in cdd_gen.sh
- **cts**（1）：Compatibility Test Suite
- **dalvik**（1）：Dalvik virtual machine and core libraries
- **dalvik2**（1）：-
- **developers/build**（1）：-
- **developers/demos**（1）：-
- **developers/docs**（1）：-
- **developers/samples**（1）：-
- **development**（1）：Platform engineering tools, sample code
- **docs/source.android.com**（1）：Source files for the source.android.com site.
- **external/AFLplusplus**（1）：American Fuzzy Lop plus plus (AFL++) Release version: 4.10c 
- **external/AntennaPod**（3）：AntennaPod This is the official repository of AntennaPod, th
- **external/ComputeLibrary**（1）：⚠ Important From release 22.05: ‘master’ branch has been rep
- **external/FP16**（1）：FP16 Header-only library for conversion to/from half-precisi
- **external/FXdiv**（1）：FXdiv Header-only library for division via fixed-point multi
- **external/ImageMagick**（1）：-
- **external/MPAndroidChart**（1）：:zap: A powerful & easy to use chart library for Android :za
- **external/Microsoft-GSL**（1）：GSL: Guidelines Support Library The Guidelines Support Libra
- **external/OpenCL-CLHPP**（1）：OpenCLTM API C++ bindings Doxgen documentation for the bindi
- **external/OpenCL-CTS**（1）：OpenCL Conformance Test Suite (CTS) This is the OpenCL CTS f
- **external/OpenCL-Headers**（1）：OpenCLTM API Headers This repository contains C language hea
- **external/OpenCL-ICD-Loader**（1）：OpenCLTM ICD Loader This repo contains the source code and t
- **external/OpenCSD**（1）：OpenCSD - An open source CoreSight(tm) Trace Decode library 
- **external/Reactive-Extensions**（1）：Bug: 74962500
- **external/TestParameterInjector**（1）：TestParameterInjector Link to Javadoc. Introduction TestPara
- **external/XNNPACK**（1）：XNNPACK XNNPACK is a highly optimized library of floating-po
- **external/aac**（1）：-
- **external/abi-compliance-checker**（1）：-
- **external/abi-dumper**（1）：-
- **external/abseil-cpp**（1）：Abseil - C++ Common Libraries The repository contains the Ab
- **external/accessibility-test-framework**（1）：Accessibility Test Framework for Android To help people with
- **external/accompanist**（1）：Accompanist is a group of libraries that aim to supplement J
- **external/adeb**（1）：Bug: 111852163
- **external/adhd**（1）：Bug: 111264136
- **external/adt-infra**（1）：-
- **external/aes**（1）：-
- **external/alac**（1）：-
- **external/android-clat**（1）：-
- **external/android-key-attestation**（1）：Android Key Attestation Library This library uses the Bouncy
- **external/android-mock**（1）：-
- **external/android-nn-driver**（1）：Arm NN Android Neural Networks driver This directory contain
- **external/android_onboarding**（1）：Bug: 299948735
- **external/androidplot**（1）：-
- **external/angle**（1）：ANGLE - Almost Native Graphics Layer Engine The goal of ANGL
- **external/annotation-tools**（1）：Bug: 67631744
- **external/anonymous-counting-tokens**（1）：An Implementation of Anonymous Counting Tokens. An anonymous
- **external/ant-glob**（1）：-
- **external/antlr**（1）：-
- **external/apache-apr**（1）：-
- **external/apache-apr-util**（1）：-
- **external/apache-commons-bcel**（1）：Apache Commons BCEL Apache Commons Bytecode Engineering Libr
- **external/apache-commons-compress**（1）：Apache Commons Compress Apache Commons Compress software def
- **external/apache-commons-io**（1）：Apache Commons IO The Apache Commons IO library contains uti
- **external/apache-commons-lang**（1）：Apache Commons Lang Apache Commons Lang, a package of Java u
- **external/apache-commons-math**（1）：-
- **external/apache-harmony**（1）：-
- **external/apache-http**（1）：-
- **external/apache-log4cxx**（1）：-
- **external/apache-velocity-engine**（1）：Title: Apache Velocity Engine Apache Velocity Welcome to Apa
- **external/apache-xml**（1）：-
- **external/apple-coreaudiosamples**（1）：-
- **external/archive-patcher**（1）：Archive Patcher Documentation Copyright 2016 Google Inc. All
- **external/arduino**（1）：-
- **external/arduino-ide**（1）：-
- **external/argp-standalone**（1）：argp-standalone This is a continuation of Niels Möller ‘s wo
- **external/arm-neon-tests**（1）：-
- **external/arm-optimized-routines**（1）：Bug: 111600065
- **external/arm-trusted-firmware**（1）：Bug: 141778450
- **external/armnn**（1）：Quick Start Guides Pre-Built Binaries Software Overview Get 
- **external/astc-codec**（1）：astc-codec astc-codec is a software ASTC decoder implementat
- **external/astl**（1）：-
- **external/auto**（1）：Auto A collection of source code generators for Java . Overv
- **external/autotest**（1）：Autotest: Automated integration testing for Android and Chro
- **external/avahi**（1）：-
- **external/avb**（1）：Android Verified Boot 2.0 This repository contains tools and
- **external/aws-crt-java**（1）：AWS CRT Java Java Bindings for the AWS Common Runtime Licens
- **external/aws-eventstream-java**（1）：AWS EventStream for Java License This library is licensed un
- **external/aws-sdk-java-v2**（1）：AWS SDK for Java 2.0 The AWS SDK for Java 2.0 is a rewrite o
- **external/bart**（1）：BART The Behavioural Analysis and Regression Toolkit is base
- **external/bazel-contrib-bazel_features**（1）：Bazel Features Use this to determine the availability of a B
- **external/bazel-contrib-rules_devicetree**（1）：Bazel rules for devicetree Ruleset for building devicetrees 
- **external/bazel-contrib-supply-chain**（1）：supply-chain
- **external/bazel-skylib**（1）：Skylib Skylib is a library of Starlark functions for manipul
- **external/bazelbuild-apple_support**（1）：Apple Support for Bazel This repository contains the Apple C
- **external/bazelbuild-bazel-central-registry**（1）：Bazel Central Registry Overview The default Bazel registry f
- **external/bazelbuild-kotlin-rules**（1）：A repository of Bazel starlark rules and tooling for Kotlin.
- **external/bazelbuild-platforms**（1）：Bazel Platforms This repository houses all canonical constra
- **external/bazelbuild-remote-apis**（1）：remote-apis This repository contains a collection of APIs wh
- **external/bazelbuild-remote-apis-sdks**（1）：Remote Execution API SDKs CI status: This repository contain
- **external/bazelbuild-rules-proto**（1）：Protobuf Rules for Bazel Postsubmit This repository contains
- **external/bazelbuild-rules_android**（1）：Android support in Bazel Disclaimer NOTE: This branch is a d
- **external/bazelbuild-rules_cc**（1）：C++ rules for Bazel Postsubmit Postsubmit + Current Bazel In
- **external/bazelbuild-rules_go**（1）：Bug: 284607415
- **external/bazelbuild-rules_java**（1）：rules_java Postsubmit Postsubmit + Current Bazel Incompatibl
- **external/bazelbuild-rules_license**（1）：rules_license CI: This repository contains a set of rules an
- **external/bazelbuild-rules_pkg**（1）：Bazel package building Bazel rules for building tar, zip, de
- **external/bazelbuild-rules_python**（1）：Python Rules for Bazel Overview This repository is the home 
- **external/bazelbuild-rules_rust**（1）：Rust Rules Postsubmit Overview This repository provides rule
- **external/bazelbuild-rules_shell**（1）：rules_shell This repository contains the Bazel ruleset for s
- **external/bazelbuild-rules_testing**（1）：Frameworks and utilities for testing Bazel Starlark rules_te
- **external/bc**（1）：bc WARNING: New user registration for https://git.gavinhowar
- **external/bcc**（1）：BPF Compiler Collection (BCC) BCC is a toolkit for creating 
- **external/bison**（1）：-
- **external/blktrace**（1）：-
- **external/bloaty**（1）：Bloaty McBloatface: a size profiler for binaries Ever wonder
- **external/bluetooth**（4）：-
- **external/bluez**（1）：-
- **external/boost**（1）：-
- **external/boringssl**（1）：-
- **external/bouncycastle**（1）：-
- **external/bpftool**（1）：This is the official home for bpftool. Please use this Githu
- **external/brotli**（1）：SECURITY NOTE Please consider updating brotli to version 1.0
- **external/bsdiff**（1）：-
- **external/bvb**（1）：-
- **external/bzip2**（1）：-
- **external/c-ares**（1）：-
- **external/caliper**（1）：-
- **external/capstone**（1）：Capstone Engine Deprecation The master branch is deprecated.
- **external/catch2**（1）：Bug: 112202352
- **external/cblas**（1）：-
- **external/cbor-java**（1）：cbor-java A Java 7 implementation of RFC 7049 : Concise Bina
- **external/cef**（1）：The Chromium Embedded Framework (CEF) is a simple framework 
- **external/ceres-solver**（1）：-
- **external/checkpolicy**（1）：-
- **external/checkstyle**（1）：Members chat: Contributors chat: Checkstyle is a tool for ch
- **external/cherry**（1）：-
- **external/chromite**（1）：-
- **external/chromium**（1）：-
- **external/chromium-crossbench**（1）：Crossbench Crossbench is a cross-browser/cross-benchmark run
- **external/chromium-libpac**（1）：-
- **external/chromium-trace**（1）：-
- **external/chromium-webview**（1）：Building the Chromium-based WebView in AOSP is no longer sup
- **external/chromium_org**（37）：#ANGLE The goal of ANGLE is to allow Windows users to seamle
- **external/chromiumos-config**（1）：ChromeOS Project Configuration Contents ChromeOS Project Con
- **external/cibu-fonts**（1）：-
- **external/clang**（1）：-
- **external/clang_35a**（1）：-
- **external/cldr**（1）：Unicode CLDR Project For current CLDR release information, s
- **external/clearsilver**（1）：-
- **external/clpeak**（1）：clpeak A synthetic benchmarking tool to measure peak capabil
- **external/cmockery**（1）：-
- **external/cn-cbor**（1）：cn-cbor: A constrained node implementation of CBOR in C Belo
- **external/codesourcery**（1）：-
- **external/collada**（1）：-
- **external/compiler-rt**（1）：-
- **external/compose-hero-benchmarks**（1）：[!TIP] If you want to see the XML version of Pokedex, check 
- **external/connectedappssdk**（1）：Connected apps is an Android feature that allows your applic
- **external/conscrypt**（1）：Conscrypt - A Java Security Provider Conscrypt is a Java Sec
- **external/coreboot**（1）：coreboot README coreboot is a Free Software project aimed at
- **external/cpu_features**（1）：cpu_features A cross-platform C library to retrieve CPU feat
- **external/cpuinfo**（1）：CPU INFOrmation library cpuinfo is a library to detect essen
- **external/crashpad**（1）：Crashpad Crashpad is a crash-reporting system. Documentation
- **external/crcalc**（1）：-
- **external/cronet**（1）：Cronet (HttpEngine) Cronet is Chrome's networking stack pack
- **external/cros**（1）：-
- **external/crosvm**（1）：crosvm - The ChromeOS Virtual Machine Monitor crosvm is a vi
- **external/cryptsetup**（1）：What the ...? Cryptsetup is utility used to conveniently set
- **external/curl**（1）：curl is a command-line tool for transferring data specified 
- **external/dagger2**（1）：Dagger A fast dependency injector for Java and Android. Dagg
- **external/dbus**（1）：-
- **external/dbus-binding-generator**（1）：-
- **external/deqp**（1）：VK-GL-CTS README This repository contains Khronos Conformanc
- **external/deqp-deps**（4）：SPIR-V Headers This repository contains machine-readable fil
- **external/desugar**（1）：-
- **external/devlib**（1）：-
- **external/dexmaker**（1）：A Java-language API for doing compile time or runtime code g
- **external/dhcpcd**（1）：-
- **external/dhcpcd-6.8.2**（1）：-
- **external/dlmalloc**（1）：b/26444982
- **external/dng_sdk**（1）：b/25605799
- **external/dnsmasq**（1）：-
- **external/doclava**（1）：-
- **external/dokka**（1）：dokka Note : This is Google's fork of Dokka, customized for 
- **external/dosfstools**（1）：-
- **external/double-conversion**（1）：https://github.com/google/double-conversion This project (do
- **external/downloader**（1）：Bug: 179417865
- **external/drm_gralloc**（1）：-
- **external/drm_hwcomposer**（1）：drm_hwcomposer Patches to drm_hwcomposer are very much welco
- **external/droiddriver**（1）：droiddriver DroidDriver is an Android UI testing library. Ja
- **external/dropbear**（1）：-
- **external/drrickorang**（1）：-
- **external/dtc**（1）：Device Tree Compiler and libfdt The source tree contains the
- **external/dwarves**（1）：Owner: android-kernel-team@google.com
- **external/dynamic_depth**（1）：Bug: 139309277
- **external/e2fsprogs**（1）：-
- **external/easymock**（1）：-
- **external/eclipse-basebuilder**（1）：-
- **external/eclipse-windowbuilder**（1）：-
- **external/edid-decode**（1）：Bug: 359896707
- **external/effcee**（1）：Effcee Effcee is a C++ library for stateful pattern matching
- **external/eigen**（1）：Eigen is a C++ template library for linear algebra: matrices
- **external/elfcopy**（1）：-
- **external/elfutils**（1）：-
- **external/emboss**（1）：Emboss Emboss is a tool for generating code that reads and w
- **external/embunit**（1）：-
- **external/emma**（1）：-
- **external/epid-sdk**（1）：Intel(R) EPID SDK The Intel(R) Enhanced Privacy ID Software 
- **external/erofs-utils**（1）：Bug: 163095736
- **external/error_prone**（1）：-
- **external/escapevelocity**（1）：EscapeVelocity summary EscapeVelocity is a templating engine
- **external/esd**（1）：-
- **external/ethtool**（1）：Bug: 137536855
- **external/executorch**（1）：ExecuTorch ExecuTorch is an end-to-end solution for enabling
- **external/exfatprogs**（1）：exfatprogs As new exfat filesystem is merged into linux-5.7 
- **external/exoplayer**（1）：Bug: 162952352
- **external/expat**（1）：-
- **external/eyes-free**（1）：-
- **external/f2fs-tools**（1）：-
- **external/faad**（1）：-
- **external/fastrpc**（1）：Bug: 144318980
- **external/fat32lib**（1）：-
- **external/fbjni**（1）：fbjni The Facebook JNI helpers library is designed to simpli
- **external/fdlibm**（1）：-
- **external/fec**（1）：-
- **external/federated-compute**（1）：Federated Compute Platform This repository hosts code for ex
- **external/fff**（1）：Fake Function Framework (fff) A Fake Function Framework for 
- **external/fft2d**（1）：Bug: 199275786
- **external/fhir**（1）：Bug: 393180809
- **external/fio**（1）：-
- **external/firebase-messaging**（1）：Bug: 199275786
- **external/flac**（1）：Free Lossless Audio Codec (FLAC) FLAC is open source softwar
- **external/flashbench**（1）：-
- **external/flashrom**（1）：Bug: 346988262
- **external/flatbuffers**（1）：FlatBuffers FlatBuffers is a cross platform serialization li
- **external/flex**（1）：This is flex, the fast lexical analyzer generator. flex is a
- **external/fmtlib**（1）：{fmt} is an open-source formatting library providing a fast 
- **external/fonttools**（1）：-
- **external/free-image**（1）：-
- **external/freetype**（1）：-
- **external/fsck_msdos**（1）：-
- **external/fsverity-utils**（1）：fsverity-utils Introduction This is fsverity-utils, a set of
- **external/ganymed-ssh2**（1）：-
- **external/gcc-demangle**（1）：-
- **external/gdata**（1）：-
- **external/gemmlowp**（1）：gemmlowp: a small self-contained low-precision GEMM library 
- **external/genext2fs**（1）：-
- **external/gentoo**（3）：-
- **external/geojson-jackson**（1）：GeoJson POJOs for Jackson A small package of all GeoJson POJ
- **external/geonames**（1）：Bug: 199275786
- **external/gflags**（1）：The documentation of the gflags library is available online 
- **external/gfxstream-protocols**（1）：Bug: 218705747
- **external/giflib**（1）：-
- **external/glide**（1）：Glide Glide is a fast and efficient open source media manage
- **external/gmmlib**（1）：Bug: 342493484
- **external/gmock**（1）：gmock has moved to external/googletest.
- **external/go-cmp**（1）：Package for equality of Go values This package is intended t
- **external/go-creachadair-shell**（1）：shell http://godoc.org/bitbucket.org/creachadair/shell The s
- **external/go-creachadair-stringset**（1）：stringset http://godoc.org/bitbucket.org/creachadair/strings
- **external/go-etree**（1）：etree The etree package is a lightweight, pure go package th
- **external/go-subcommands**（1）：subcommands Subcommands is a Go package that implements a si
- **external/golang-glog**（1）：glog Leveled execution logs for Go. This is an efficient pur
- **external/golang-klauspost-compress**（1）：compress This package provides various compression algorithm
- **external/golang-pkg-xattr**（1）：xattr Extended attribute support for Go (linux + darwin + fr
- **external/golang-protobuf**（1）：Go support for Protocol Buffers This project hosts the Go im
- **external/golang-x-sync**（1）：Go Sync This repository provides Go concurrency primitives i
- **external/golang-x-sys**（1）：sys This repository holds supplemental Go packages for low-l
- **external/golang-x-tools**（1）：Go Tools This repository provides the golang.org/x/tools mod
- **external/google-auth-library-java**（1）：Google Auth Library Open source authentication client librar
- **external/google-benchmark**（1）：Benchmark A library to benchmark code snippets, similar to u
- **external/google-breakpad**（1）：Breakpad Breakpad is a set of client and server components w
- **external/google-cloud-java**（1）：Google Cloud Java Client Libraries Java idiomatic client for
- **external/google-diff-match-patch**（1）：-
- **external/google-fonts**（15）：Bug: 121039455
- **external/google-fruit**（1）：Fruit is a dependency injection framework for C++, loosely i
- **external/google-java-format**（1）：google-java-format google-java-format is a program that refo
- **external/google-smali**（1）：About smali/baksmali is an assembler/disassembler for the de
- **external/google-styleguide**（1）：Google Style Guides Every major open-source project has its 
- **external/google-tv-pairing-protocol**（1）：-
- **external/google-uuid**（1）：uuid The uuid package generates and inspects UUIDs based on 
- **external/googleapis**（1）：Google APIs This repository contains the original interface 
- **external/googleapis-enterprise-certificate-proxy**（1）：Google Proxies for Enterprise Certificates (Preview) Certifi
- **external/googleclient**（1）：-
- **external/googletest**（1）：GoogleTest Announcements Live at Head GoogleTest now follows
- **external/gptfdisk**（1）：-
- **external/gradle-perf-android-medium**（1）：WordPress for Android If you‘re just looking to install Word
- **external/grpc-grpc**（1）：gRPC – An RPC library and framework gRPC is a modern, open s
- **external/grpc-grpc-java**（1）：gRPC-Java - An RPC library and framework Supported Platforms
- **external/grub**（1）：-
- **external/gsc-utils**（1）：Bug: 361398570
- **external/gsoap**（1）：-
- **external/gson**（1）：Gson Gson is a Java library that can be used to convert Java
- **external/gtest**（1）：-
- **external/gturri-aXMLRPC**（1）：What is aXMLRPC? aXMLRPC is a Java library with a leightweig
- **external/gturri-jISO8601**（1）：Overview jISO8601 is yet another library made to parse dates
- **external/guava**（1）：Guava: Google Core Libraries for Java Guava is a set of core
- **external/guice**（1）：Guice Latest release: 4.1 Documentation: User Guide , 4.1 ja
- **external/gwp_asan**（1）：Bug: 139531572
- **external/hafnium**（1）：Hafnium Hafnium is the Secure Partition Manager(SPM) referen
- **external/hamcrest**（1）：Java Hamcrest Licensed under BSD License . What is Hamcrest?
- **external/harfbuzz**（1）：-
- **external/harfbuzz_ng**（1）：HarfBuzz HarfBuzz is a text shaping engine. It primarily sup
- **external/honggfuzz**（1）：Bug: 111264136
- **external/hsqldb**（1）：-
- **external/hyphenation**（1）：-
- **external/hyphenation-patterns**（1）：-
- **external/iamf_tools**（1）：iamf-tools What is IAMF? The Immersive Audio Model and Forma
- **external/icing**（1）：Icing Search Library Icing is a fast, embedded, mobile-frien
- **external/icu**（1）：-
- **external/icu4c**（1）：-
- **external/id3lib**（1）：-
- **external/igt-gpu-tools**（1）：IGT GPU Tools Description IGT GPU Tools is a collection of t
- **external/image_io**（1）：Bug: 139309277
- **external/ims**（1）：-
- **external/ink-stroke-modeler**（1）：Ink Stroke Modeler This library smooths raw freehand input a
- **external/intel-media-driver**（1）：Bug: 352643499
- **external/iosched**（1）：This is a fork of https://github.com/google/iosched in order
- **external/iperf3**（1）：iperf3: A TCP, UDP, and SCTP network bandwidth measurement t
- **external/iproute2**（1）：-
- **external/ipsec-tools**（1）：-
- **external/iptables**（1）：-
- **external/iputils**（1）：-
- **external/iw**（1）：-
- **external/jackson-annotations**（1）：Overview This project contains general purpose annotations f
- **external/jackson-core**（1）：Overview This project contains core low-level incremental (“
- **external/jackson-databind**（1）：Overview This project contains the general-purpose data-bind
- **external/jacoco**（1）：JaCoCo Java Code Coverage Library JaCoCo is a free Java code
- **external/jakarta.inject**（1）：Bug: 383313386
- **external/jarjar**（1）：-
- **external/javaparser**（1）：JavaParser This project contains a set of libraries implemen
- **external/javapoet**（1）：JavaPoet JavaPoet is a Java API for generating .java source 
- **external/javasqlite**（1）：-
- **external/javassist**（1）：Java bytecode engineering toolkit Javassist version 3 Copyri
- **external/jazzer-api**（1）：Website | Blog | Twitter Jazzer is a coverage-guided, in-pro
- **external/jcommander**（1）：b/27552463
- **external/jdiff**（1）：-
- **external/jemalloc**（1）：-
- **external/jemalloc_new**（1）：Bug: 68660095
- **external/jenkins-hash**（1）：-
- **external/jetbrains**（10）：Welcome to JetBrains Runtime! JetBrains Runtime is a fork of
- **external/jetpack-camera-app**（1）：Jetpack Camera App 📸 Jetpack Camera App (JCA) is a camera ap
- **external/jetty**（1）：-
- **external/jhead**（1）：-
- **external/jimfs**（1）：Jimfs Jimfs is an in-memory file system for Java 7 and above
- **external/jline**（1）：-
- **external/jmdns**（1）：-
- **external/jmonkeyengine**（1）：-
- **external/jpeg**（1）：-
- **external/jsilver**（1）：-
- **external/jsmn**（1）：JSMN jsmn (pronounced like ‘jasmine’) is a minimalistic JSON
- **external/json-schema-validator**（1）：Stack Overflow | Google Group | Gitter Chat | Subreddit | Yo
- **external/jsoncpp**（1）：JsonCpp JSON is a lightweight data-interchange format. It ca
- **external/jsoup**（1）：jsoup: Java HTML Parser jsoup is a Java library that makes i
- **external/jsoup-1p-stubs**（1）：Bug: 357762254
- **external/jspecify**（1）：JSpecify An artifact of well-specified annotations to power 
- **external/jsr305**（1）：-
- **external/jsr330**（1）：b/27552463
- **external/junit**（1）：JUnit 4 JUnit is a simple framework to write repeatable test
- **external/junit-params**（1）：JUnitParams Parameterised tests that don't suck Example @Run
- **external/kernel-headers**（1）：Android kernel headers This project contains the original ke
- **external/kmod**（1）：kmod - Linux kernel module handling Information Mailing list
- **external/kotlin-compose-compiler**（1）：Bug: 340243044
- **external/kotlin.metadata**（1）：Bug: 383596474
- **external/kotlinc**（1）：-
- **external/kotlinpoet**（1）：KotlinPoet KotlinPoet is a Kotlin and Java API for generatin
- **external/kotlinx.atomicfu**（1）：AtomicFU Note on Beta status: the plugin is in its active de
- **external/kotlinx.coroutines**（1）：kotlinx.coroutines Library support for Kotlin coroutines wit
- **external/kotlinx.metadata**（1）：Bug: 159272084
- **external/kotlinx.serialization**（1）：Kotlin multiplatform / multi-format reflectionless serializa
- **external/ksoap2**（1）：-
- **external/ksp**（1）：Kotlin Symbol Processing API Welcome to KSP! Kotlin Symbol P
- **external/ktfmt**（1）：ktfmt ktfmt is a program that pretty-prints (formats) Kotlin
- **external/ktlint**（1）：Features: No configuration. Which means no decisions to make
- **external/kythe**（1）：Bug: 135923310
- **external/lame**（1）：-
- **external/leakcanary2**（1）：LeakCanary 🐤 A memory leak detection library for Android. sq
- **external/leveldb**（1）：LevelDB is a fast key-value storage library written at Googl
- **external/libabigail**（1）：This libabigail repository is unmaintained Android no longer
- **external/libaom**（1）：README.md AV1 Codec Library Contents Building the lib and ap
- **external/libavc**（1）：LIBAVC Getting Started Document LibAVC build steps Supports:
- **external/libbackup**（1）：-
- **external/libbpf**（1）：libbpf This is the official home of the libbpf library. Plea
- **external/libbrillo**（1）：libbrillo: platform utility library libbrillo is a shared li
- **external/libcap**（1）：-
- **external/libcap-ng**（1）：libcap-ng The libcap-ng library should make programming with
- **external/libchrome**（1）：-
- **external/libchrome-gestures**（1）：Bug: 254465942
- **external/libchromeos**（1）：Bug: 25417586

(DEAD) Code migrated to platform/external/lib
- **external/libchromeos-rs**（1）：libchromeos-rs - The Rust crate for common Chrome OS code li
- **external/libconfig**（1）：libconfig C/C++ library for processing structured configurat
- **external/libconstrainedcrypto**（1）：b/27293141
- **external/libcppbor**（1）：LibCppBor: A Modern C++ CBOR Parser and Generator LibCppBor 
- **external/libcups**（1）：README - Apple CUPS v2.3.6 - 2022-05-25 Note: Apple CUPS is 
- **external/libcxx**（1）：-
- **external/libcxx_35a**（1）：-
- **external/libcxxabi**（1）：-
- **external/libcxxabi_35a**（1）：-
- **external/libcxxrt**（1）：-
- **external/libdaemon**（1）：-
- **external/libdav1d**（1）：dav1d dav1d is an AV1 cross-platform d ecoder, open-source, 
- **external/libdisplay-info**（1）：libdisplay-info EDID and DisplayID library. Goals: Provide a
- **external/libdivsufsort**（1）：libdivsufsort libdivsufsort is a software library that imple
- **external/libdrm**（1）：-
- **external/libedit**（1）：-
- **external/libepoxy**（1）：Epoxy is a library for handling OpenGL function pointer mana
- **external/libese**（1）：libese Document last updated: 13 Jan 2017 Introduction libes
- **external/libevent**（1）：0. BUILDING AND INSTALLATION (Briefly) Autoconf $ ./configur
- **external/libexif**（1）：-
- **external/libffi**（1）：Status libffi-3.3 was released on November 23, 2019. Check t
- **external/libfuse**（1）：libfuse About FUSE (Filesystem in Userspace) is an interface
- **external/libgav1**（1）：libgav1 -- an AV1 decoder libgav1 is a Main profile (0), Hig
- **external/libgdx**（1）：libGDX is a cross-platform Java game development framework b
- **external/libgsm**（1）：-
- **external/libhevc**（1）：LIBHEVC Getting Started Document LibHEVC build steps Support
- **external/libiio**（1）：Bug: 162952352
- **external/libjpeg-turbo**（1）：Background libjpeg-turbo is a JPEG image codec that uses SIM
- **external/libkmsxx**（1）：kms++ - C++ library for kernel mode setting kms++ is a C++17
- **external/liblc3**（1）：Low Complexity Communication Codec (LC3) LC3 and LC3 Plus ar
- **external/libldac**（1）：-
- **external/liblzf**（1）：-
- **external/libmicrohttpd**（1）：-
- **external/libmojo**（1）：This repository was migrated into libchrome.
- **external/libmonet**（1）：Bug: 210903235
- **external/libmpeg2**（1）：-
- **external/libmtp**（1）：-
- **external/libnetfilter_conntrack**（1）：-
- **external/libnfc-nci**（1）：-
- **external/libnfc-nxp**（1）：-
- **external/libnfnetlink**（1）：-
- **external/libnl**（1）：-
- **external/libnl-headers**（1）：-
- **external/libogg**（1）：Ogg Ogg project codecs use the Ogg bitstream format to arran
- **external/libopenapv**（1）：OpenAPV (Open Advanced Professional Video Codec) OpenAPV pro
- **external/libopus**（1）：-
- **external/liboqs**（1）：CircleCI : , TravisCI : liboqs liboqs is an open source C li
- **external/libpalmrejection**（1）：Bug: 216210262
- **external/libpcap**（1）：LIBPCAP 1.x.y by The Tcpdump Group To report a security issu
- **external/libpciaccess**（1）：xorg/lib/libpciaccess - Generic PCI access library Documenta
- **external/libphonenumber**（1）：-
- **external/libpng**（1）：-
- **external/libppp**（1）：-
- **external/libprotobuf-mutator**（1）：libprotobuf-mutator Overview libprotobuf-mutator is a librar
- **external/libsepol**（1）：-
- **external/libsrtp2**（1）：Introduction to libSRTP This package provides an implementat
- **external/libtextclassifier**（1）：-
- **external/libtraceevent**（1）：Bug: 227522263
- **external/libtracefs**（1）：Bug: 227522878
- **external/libultrahdr**（1）：Introduction libultrahdr is an image compression library tha
- **external/libunwind**（1）：-
- **external/libunwind_llvm**（1）：-
- **external/liburing**（1）：Bug: 193475142
- **external/libusb**（1）：-
- **external/libusb-compat**（1）：-
- **external/libusb_aah**（1）：-
- **external/libutf**（1）：-
- **external/libva**（1）：Libva Project Libva is an implementation for VA-API (Video A
- **external/libva-utils**（1）：Libva-utils Project libva-utils is a collection of utilities
- **external/libvncserver**（1）：-
- **external/libvorbis**（1）：-
- **external/libvpx**（1）：-
- **external/libvterm**（1）：-
- **external/libweave**（1）：Overview libWeave is the library with device side implementa
- **external/libwebm**（1）：Bug: 173644001
- **external/libwebsockets**（1）：Libwebsockets Libwebsockets is a simple-to-use, MIT-license,
- **external/libxaac**（1）：Introduction to libxaac Extended HE-AAC, the latest innovati
- **external/libxcam**（1）：libXCam Copyright (C) 2014-2019 Intel Corporation libxcam co
- **external/libxkbcommon**（1）：libxkbcommon libxkbcommon is a keyboard keymap compiler and 
- **external/libxml2**（1）：libxml2 libxml2 is an XML toolkit implemented in C, original
- **external/libxslt**（1）：-
- **external/libyuv**（1）：libyuv is an open source project that includes YUV scaling a
- **external/licenseclassifier**（1）：License Classifier Introduction The license classifier is a 
- **external/linux-firmware**（1）：About the linux-firmware project Please be aware that this p
- **external/linux-kselftest**（1）：-
- **external/linux-tools-perf**（1）：See system/extras/simpleperf/ instead.
- **external/lisa**（1）：NOTE : This is still a work in progress project, suitable fo
- **external/lldb**（1）：Not yet needed
- **external/lldb-utils**（1）：-
- **external/llvm**（1）：-
- **external/llvm-libc**（1）：Bug: 321313756
- **external/llvm_35a**（1）：-
- **external/lmfit**（1）：-
- **external/login-items-ae**（1）：-
- **external/lohit-fonts**（1）：-
- **external/lottie**（1）：Lottie for Android, iOS , React Native , Web , and Windows L
- **external/ltp**（1）：-
- **external/ltrace**（1）：-
- **external/lua**（1）：Bug: 120607669
- **external/lvm2**（1）：-
- **external/lz4**（1）：LZ4 - Extremely fast compression LZ4 is lossless compression
- **external/lzma**（1）：7-Zip on GitHub 7-Zip website: 7-zip.org
- **external/lzop**（1）：-
- **external/marisa-trie**（1）：README Project name marisa-trie Project summary MARISA: Matc
- **external/markdown**（1）：-
- **external/mbedtls**（1）：README for Mbed TLS Mbed TLS is a C library that implements 
- **external/mdnsresponder**（1）：-
- **external/mesa3d**（1）：-
- **external/messageformat**（1）：-
- **external/mime-support**（1）：Bug: 138443287
- **external/minigbm**（1）：-
- **external/minijail**（1）：Minijail The Minijail homepage is https://google.github.io/m
- **external/mksh**（1）：-
- **external/mmc-utils**（1）：-
- **external/mobile-data-download**（1）：Bug: 236694189
- **external/mobly-bundled-snippets**（1）：Mobly Bundled Snippets is a set of Snippets to allow Mobly t
- **external/mobly-snippet-lib**（1）：Getting Started with Snippets for Mobly Mobly Snippet Lib is
- **external/mockftpserver**（1）：-
- **external/mockito**（1）：-
- **external/mockito-kotlin**（1）：Mockito-Kotlin A small library that provides helper function
- **external/mockwebserver**（1）：-
- **external/modp_b64**（1）：-
- **external/moltenvk**（1）：MoltenVK Copyright (c) 2015-2024 The Brenwill Workshop Ltd. 
- **external/moshi**（1）：Moshi Moshi is a modern JSON library for Android, Java and K
- **external/mp4parser**（1）：-
- **external/mp4v2**（1）：-
- **external/mpdecimal**（1）：Bug: 390479029
- **external/mpg123**（1）：-
- **external/ms-tpm-20-ref**（1）：Official TPM 2.0 Reference Implementation (by Microsoft) Thi
- **external/mtools**（1）：Bug: 180112530
- **external/musl**（1）：Bug: 191701391
- **external/n2**（1）：n2, an alternative ninja implementation n2 (pronounced “into
- **external/nanohttpd**（1）：NanoHTTPD – a tiny web server in Java NanoHTTPD is a light-w
- **external/nanopb-c**（1）：Nanopb - Protocol Buffers for Embedded Systems Nanopb is a s
- **external/nanoprintf**（1）：nanoprintf nanoprintf is an unencumbered implementation of s
- **external/naver-fonts**（1）：-
- **external/ncurses**（1）：Bug: 173536531
- **external/neon_2_sse**（1）：The NEON_2_SSE.h file is intended to simplify ARM->IA32 port
- **external/netcat**（1）：-
- **external/netperf**（1）：-
- **external/neven**（1）：-
- **external/newfs_msdos**（1）：Bug: 110053628
- **external/nfacct**（1）：-
- **external/ninja**（1）：-
- **external/nist-pkits**（1）：-
- **external/nist-sip**（1）：-
- **external/nos**（3）：Android components for Nugget Android communicates with Nugg
- **external/noto-fonts**（1）：-
- **external/nsjail**（1）：Overview What forms of isolation does it provide Which use-c
- **external/nullaway**（1）：NullAway: Fast Annotation-Based Null Checking for Java NullA
- **external/oauth**（1）：-
- **external/obex**（1）：Bug: 219989416
- **external/objenesis**（1）：-
- **external/oboe**（1）：Oboe Oboe is a C++ library which makes it easy to build high
- **external/obstack**（1）：Bug: 201358331
- **external/oj-libjdwp**（1）：Bug: 62821960
- **external/okhttp**（1）：OkHttp An HTTP & SPDY client for Android and Java applicatio
- **external/okio**（1）：Okio See the project website for documentation and APIs. Oki
- **external/one-true-awk**（1）：The One True Awk This is the version of awk described in The
- **external/open-dice**（1）：Open Profile for DICE This repository contains the specifica
- **external/open-vcdiff**（1）：-
- **external/opencensus-java**（1）：Warning OpenCensus and OpenTracing have merged to form OpenT
- **external/opencore**（1）：OpenCORE Media Framework
- **external/opencv**（1）：-
- **external/opencv3**（1）：OpenCV: Open Source Computer Vision Library Resources Homepa
- **external/openfst**（1）：-
- **external/openscreen**（1）：Open Screen Library The Open Screen Library implements the O
- **external/openssh**（1）：Portable OpenSSH OpenSSH is a complete implementation of the
- **external/openssl**（1）：This OpenSSL repository is unmaintained Android no longer us
- **external/openthread**（1）：What is OpenThread? OpenThread released by Google is... ...a
- **external/openwrt-prebuilts**（1）：Bug: 201358034
- **external/oprofile**（1）：-
- **external/oss-fuzz**（1）：Bug: 141203588
- **external/ot-br-posix**（1）：OpenThread Border Router Per the Thread Specification , a Th
- **external/ow2-asm**（1）：Bug: 259118989
- **external/owasp**（2）：OWASP Java Encoder Project Contextual Output Encoding is a c
- **external/pandora**（3）：See https://developers.google.com/pandora/guides/avatar/andr
- **external/parameter-framework**（1）：-
- **external/pciutils**（1）：Bug: 346990074
- **external/pcre**（1）：PCRE2 - Perl-Compatible Regular Expressions The PCRE2 librar
- **external/pdfium**（1）：PDFium Prerequisites PDFium uses the same build tooling as C
- **external/perf_data_converter**（1）：Introduction The perf_to_profile binary can be used to turn 
- **external/perfetto**（1）：Perfetto - System profiling, app tracing and trace analysis 
- **external/perfmark**（1）：PerfMark PerfMark is a low-overhead, manually-instrumented, 
- **external/pffft**（1）：PFFFT: a pretty fast FFT and fast convolution with PFFASTCON
- **external/piex**（1）：b/26535406
- **external/pigweed**（1）：Pigweed Pigweed is an open source collection of embedded-tar
- **external/pigz**（1）：Bug: 316037781
- **external/pixman**（1）：-
- **external/ply**（1）：-
- **external/ppp**（1）：-
- **external/private-join-and-compute**（1）：Private Join and Compute This project contains an implementa
- **external/proguard**（1）：-
- **external/protobuf**（1）：Protocol Buffers - Google's data interchange format Copyrigh
- **external/protobuf-javalite**（1）：Bug: 118344251
- **external/psimd**（1）：Bug: 148898539
- **external/pthreadpool**（1）：pthreadpool pthreadpool is a portable and efficient thread p
- **external/pthreads**（1）：-
- **external/puffin**（1）：Puffin: A deterministic deflate re-compressor (for patching 
- **external/python**（77）：Abseil Python Common Libraries This repository is a collecti
- **external/pytorch**（1）：PyTorch is a Python package that provides two high-level fea
- **external/qemu**（1）：-
- **external/qemu-android**（1）：-
- **external/qemu-pc-bios**（1）：-
- **external/qt**（1）：-
- **external/quake**（1）：-
- **external/r8**（1）：D8 dexer and R8 shrinker The R8 repo contains two tools: D8 
- **external/rapidjson**（1）：A fast JSON parser/generator for C++ with both SAX/DOM style
- **external/rappor**（1）：RAPPOR RAPPOR is a novel privacy technology that allows infe
- **external/regex-re2**（1）：-
- **external/renderscript-intrinsics-replacement-toolkit**（1）：RenderScript Intrinsics Replacement Toolkit - v0.8 BETA This
- **external/replicaisland**（1）：-
- **external/rmi4utils**（1）：-
- **external/rnnoise**（1）：Bug: 159235102
- **external/robolectric**（1）：Robolectric is the industry-standard unit testing framework 
- **external/robolectric-shadows**（1）：Robolectric is the industry-standard unit testing framework 
- **external/roboto-flex-fonts**（1）：Bug: 276927805
- **external/roboto-fonts**（1）：-
- **external/rootdev**（1）：-
- **external/rules_pkg**（1）：MOVED This repository is deprecated and moved to platform/ex
- **external/rust**（441）：3rd party Rust crates from crates.io This repository contain
- **external/ruy**（1）：The ruy matrix multiplication library This is not an officia
- **external/s2-geometry-library-java**（1）：Bug: 199275786
- **external/safe-iop**（1）：-
- **external/sandboxed-api**（1）：Copyright 2019-2023 Google LLC What is Sandboxed API? The Sa
- **external/scapy**（1）：Scapy Scapy is a powerful Python-based interactive packet ma
- **external/scrypt**（1）：-
- **external/scudo**（1）：Bug: 140939296
- **external/sdk-platform-java**（1）：This repository consists of the following modules: gapic-gen
- **external/sdv**（1）：vsomeip Copyright Copyright (C) 2015-2017, Bayerische Motore
- **external/seccomp-tests**（1）：Seccomp-BPF Kernel Self-Test Suite This repository contains 
- **external/selinux**（1）：SELinux Userspace SELinux is a flexible Mandatory Access Con
- **external/sepolicy**（1）：-
- **external/setfilters**（1）：Set filters library This repository contains implementations
- **external/setupcompat**（1）：Bug: 119302147
- **external/setupdesign**（1）：Bug: 139309277
- **external/sfntly**（1）：sfntly This project is not developed any further. Only Bug f
- **external/sg3_utils**（1）：Bug: 257494669
- **external/shaderc**（4）：Also see the Khronos landing page for glslang as a reference
- **external/shflags**（1）：shFlags README shFlags is a port of the Google gflags librar
- **external/sil-fonts**（1）：-
- **external/skia**（1）：-
- **external/skqp**（1）：Bug: 72556177
- **external/sl4a**（1）：Scripting Layer For Android Introduction Originally authored
- **external/slf4j**（1）：About SLF4J The Simple Logging Facade for Java (SLF4J) serve
- **external/smack**（1）：-
- **external/smali**（1）：About smali/baksmali is an assembler/disassembler for the de
- **external/snakeyaml**（1）：The art of simplicity is a puzzle of complexity. Overview YA
- **external/sonic**（1）：-
- **external/sonivox**（1）：-
- **external/spdx-tools**（1）：SPDX tools-golang tools-golang is a collection of Go package
- **external/speex**（1）：-
- **external/spirv-llvm**（1）：-
- **external/sqlite**（1）：SQLite database engine (http://sqlite.org)
- **external/squashfs-tools**（1）：-
- **external/srec**（1）：-
- **external/stardoc**（1）：Bug: 194825758
- **external/starlark-go**（1）：Starlark in Go This is the home of the Starlark in Go projec
- **external/stg**（1）：Symbol-Type Graph (STG) The STG (symbol-type graph) is an AB
- **external/stlport**（1）：-
- **external/strace**（1）：-
- **external/stressapptest**（1）：stressapptest Stressful Application Test (or stressapptest, 
- **external/subsampling-scale-image-view**（1）：Subsampling Scale Image View A custom image view for Android
- **external/svox**（1）：-
- **external/swiftshader**（1）：SwiftShader Introduction SwiftShader[^1] is a high-performan
- **external/swig**（1）：-
- **external/syslinux**（1）：-
- **external/syspatch**（1）：-
- **external/syzkaller**（1）：syzkaller - kernel fuzzer syzkaller is an unsupervised cover
- **external/tagsoup**（1）：-
- **external/tcpdump**（1）：TCPDUMP 4.x.y by The Tcpdump Group To report a security issu
- **external/tensorflow**（1）：Documentation TensorFlow is an end-to-end open source platfo
- **external/tesseract**（1）：Tesseract Open Source OCR Engine
- **external/testng**（1）：![Java9 EA Build Status](https://img.shields.io/jenkins/s/ht
- **external/tflite-support**（1）：TensorFlow Lite Support TFLite Support is a toolkit that hel
- **external/threetenbp**（1）：ThreeTen backport project JSR-310 provides a new date and ti
- **external/timezone-boundary-builder**（1）：Timezone Boundary Builder The goal of this project is to pro
- **external/timezonepicker-support**（1）：-
- **external/tink**（1）：Tink A multi-language, cross-platform library that provides 
- **external/tink-java**（1）：Tink Java Test GCP Ubuntu MacOS Bazel Maven N/A Using crypto
- **external/tinyalsa**（1）：-
- **external/tinyalsa_new**（1）：TinyALSA TinyALSA is a small library to interface with ALSA 
- **external/tinycompress**（1）：-
- **external/tinyobjloader**（1）：tinyobjloader https://github.com/syoyo/tinyobjloader Tiny bu
- **external/tinyxml**（1）：-
- **external/tinyxml2**（1）：TinyXML-2 TinyXML-2 is a simple, small, efficient, C++ XML p
- **external/tlsdate**（1）：-
- **external/toolchain-utils**（1）：toolchain-utils Various utilities used by the ChromeOS toolc
- **external/toybox**（1）：-
- **external/tpm2**（1）：-
- **external/tpm2-tss**（1）：Overview This repository hosts source code implementing the 
- **external/trace-cmd**（1）：Bug: 227522675
- **external/trappy**（1）：TRAPpy TRAPpy (Trace Analysis and Plotting in Python) is a v
- **external/tremolo**（1）：-
- **external/tremor**（1）：-
- **external/truth**（1）：What is Truth? Truth makes your test assertions and failure 
- **external/turbine**（1）：Turbine Turbine is a header compiler for Java.
- **external/u-boot**（1）：-
- **external/ublksrv**（1）：Bug: 376130584
- **external/ukey2**（1）：Bug: 123365555
- **external/unicode**（1）：-
- **external/universal-tween-engine**（1）：-
- **external/usrsctp**（1）：usrsctp This is a userland SCTP stack supporting FreeBSD, Li
- **external/utf8proc**（1）：-
- **external/uwb**（1）：Bug: 237676695
- **external/v4l-utils**（1）：v4l-utils Linux utilities and libraries to handle media devi
- **external/v4l2_codec2**（1）：General Information Scope of this document This document is 
- **external/v8**（1）：V8 JavaScript Engine V8 is Google's open source JavaScript e
- **external/valgrind**（1）：-
- **external/vboot_reference**（1）：-
- **external/virglrenderer**（1）：Bug: 111504385
- **external/virtio-media**（1）：Virtio-media This is a virtio protocol definition, companion
- **external/vixl**（1）：VIXL: ARMv8 Runtime Code Generation Library 8.0.0 Contents: 
- **external/vm_tools**（1）：Bug: 171318426
- **external/vogar**（1）：Vogar Vogar is a generic code/test/benchmark runner tool for
- **external/volley**（1）：Volley Volley is an HTTP library that makes networking for A
- **external/vulkan-headers**（1）：Vulkan-Headers Vulkan header files and API registry This rep
- **external/vulkan-tools**（1）：Vulkan Ecosystem Components This project provides Khronos of
- **external/vulkan-validation-layers**（1）：Vulkan Ecosystem Components This project provides the Khrono
- **external/walt**（1）：WALT Latency Timer DISCLAIMER: This is not an official Googl
- **external/wayland**（1）：Wayland Wayland is a project to define a protocol for a comp
- **external/wayland-protocols**（1）：Bug: 111264136
- **external/weave-common**（1）：Weave Common code This repository will contain code common t
- **external/webkit**（1）：-
- **external/webp**（1）：WebP Codec __ __ ____ ____ ____ / \\/ \/ _ \/ _ )/ _ \ \ / _
- **external/webrtc**（1）：WebRTC is a free, open software project that provides browse
- **external/webrtc_legacy**（1）：WebRTC is a free, open software project that provides browse
- **external/webview_support_interfaces**（1）：Bug: 69806605
- **external/wmediumd**（1）：Introduction This is a wireless medium simulation tool for L
- **external/wpa_supplicant**（1）：-
- **external/wpa_supplicant_6**（1）：-
- **external/wpa_supplicant_8**（1）：-
- **external/wuffs-mirror-release-c**（1）：Wuffs Mirror (release/c) This repository mirrors a subset of
- **external/wycheproof**（1）：Project Wycheproof https://github.com/google/wycheproof Proj
- **external/x264**（1）：-
- **external/xdelta3**（1）：-
- **external/xerces-cpp**（1）：-
- **external/xmlrpcpp**（1）：-
- **external/xmlwriter**（1）：-
- **external/xmp_toolkit**（1）：-
- **external/xz-embedded**（1）：-
- **external/xz-java**（1）：Bug: 122833812
- **external/yaffs2**（1）：-
- **external/yapf**（1）：YAPF Introduction YAPF is a Python formatter based on clang-
- **external/zlib**（1）：-
- **external/zopfli**（1）：-
- **external/zstd**（1）：Zstandard , or zstd as short version, is a fast lossless com
- **external/zucchini**（1）：Basic Definitions for Patching Binary : Executable image and
- **external/zxing**（1）：Project in Maintenance Mode Only The project is in maintenan
- **frameworks/av**（1）：-
- **frameworks/base**（1）：Android framework classes and services
- **frameworks/compile**（5）：-
- **frameworks/data-binding**（1）：-
- **frameworks/ex**（1）：-
- **frameworks/hardware**（1）：-
- **frameworks/janktesthelper**（1）：-
- **frameworks/layoutlib**（1）：-
- **frameworks/libs**（7）：Berberis Dynamic binary translator to run Android apps with 
- **frameworks/media**（1）：-
- **frameworks/minikin**（1）：-
- **frameworks/ml**（1）：-
- **frameworks/multidex**（1）：-
- **frameworks/native**（1）：-
- **frameworks/opt**（26）：Bug: 72656027
- **frameworks/policies**（1）：-
- **frameworks/proto_logging**（1）：Bug: 143080132
- **frameworks/rs**（1）：-
- **frameworks/support**（1）：This branch of this repository is no longer in use. See the 
- **frameworks/testing**（1）：-
- **frameworks/uiautomator**（1）：-
- **frameworks/volley**（1）：-
- **frameworks/webview**（1）：-
- **frameworks/wilhelm**（1）：-
- **gdk**（1）：-
- **hardware/akm**（1）：-
- **hardware/broadcom**（2）：-
- **hardware/bsp**（22）：Bug: 120215675
- **hardware/google**（19）：AEMU library This is an utility library for common functions
- **hardware/intel**（13）：-
- **hardware/interfaces**（1）：-
- **hardware/invensense**（1）：-
- **hardware/knowles**（1）：Bug: 141248619
- **hardware/libhardware**（1）：hardware abstraction library
- **hardware/libhardware_legacy**（1）：-
- **hardware/marvell**（1）：-
- **hardware/mediatek**（1）：-
- **hardware/msm7k**（1）：msm7k hardware glue
- **hardware/nxp**（5）：Bug: 244369531
- **hardware/qcom**（48）：Bug: 72567981
- **hardware/ril**（1）：radio interface layer
- **hardware/samsung**（1）：Bug: 179437419
- **hardware/samsung_slsi**（1）：-
- **hardware/st**（3）：HAL st21nfc HAL
- **hardware/synaptics**（1）：Bug: 226894942
- **hardware/telink**（1）：Bug: 153349145
- **hardware/ti**（6）：Bug: 111362717
- **libcore**（1）：Android Core Library Existing open bugs File a new bug File 
- **libcore2**（1）：-
- **libnativehelper**（1）：libnativehelper libnativehelper is a collection of JNI relat
- **manifest**（1）：Android Platform Manifest
- **media/cts**（1）：Bug: 177363648
- **ndk**（1）：Android Native Development Kit (NDK) The latest version of t
- **packages/apps**（115）：Bug: 335805767
- **packages/experimental**（1）：-
- **packages/inputmethods**（4）：Default keyboard for Android TV
- **packages/modules**（42）：ANGLE for Android Readme Additional ANGLE developer instruct
- **packages/providers**（17）：Content provider for calendar data
- **packages/screensavers**（3）：-
- **packages/services**（9）：Bug: 115934920
- **packages/wallpapers**（8）：-
- **pdk**（1）：-
- **platform_testing**（1）：-
- **prebuilt**（1）：binaries to support linux and osx builds
- **prebuilts/abi-dumps**（3）：Bug: 79424996
- **prebuilts/android-emulator**（1）：-
- **prebuilts/android-emulator-build**（7）：Bug: 234635748
- **prebuilts/androidx**（2）：Bug: 110713131
- **prebuilts/asuite**（1）：Bug: 114274040
- **prebuilts/bazel**（3）：Updating the Bazel prebuilts in AOSP Instructions First, dec
- **prebuilts/build-tools**（1）：prebuilts/build-tools See https://go/android-build-system-te
- **prebuilts/bundletool**（1）：Bug: 119496442
- **prebuilts/checkcolor**（1）：Lint check for hardcoded colors What is this lint check for 
- **prebuilts/checkstyle**（1）：Checkstyle Checkstyle is used by developers to validate Java
- **prebuilts/clang**（14）：Android Clang/LLVM Prebuilts For the latest version of this 
- **prebuilts/clang-tools**（1）：Prebuilts for Clang/LLVM-based tools used in Android For the
- **prebuilts/cmake**（3）：-
- **prebuilts/cmdline-tools**（1）：Bug: 157688620
- **prebuilts/deqp**（1）：-
- **prebuilts/devtools**（1）：-
- **prebuilts/eclipse**（1）：Prebuilt packages from the Eclipse project, used to build co
- **prebuilts/eclipse-build-deps**（1）：-
- **prebuilts/fuchsia_sdk**（1）：Fuchsia SDK This directory contains a subset of the Fuchsia 
- **prebuilts/fullsdk**（16）：Bug: 273147633
- **prebuilts/fullsdk-darwin**（10）：Bug: 222299323
- **prebuilts/fullsdk-linux**（11）：Bug: 222299323
- **prebuilts/gas**（1）：platform/prebuilts/gas/linux-x86 This repository exists as a
- **prebuilts/gcc**（47）：Host glibc sysroot Here lie the bones of a prebuilt glibc 2.
- **prebuilts/gdb**（2）：-
- **prebuilts/go**（3）：The Go Programming Language Go is an open source programming
- **prebuilts/gradle-plugin**（1）：-
- **prebuilts/jdk**（6）：Bug: 141376136
- **prebuilts/ktlint**（1）：Bug: 111366828
- **prebuilts/libprotobuf**（1）：-
- **prebuilts/libs**（1）：-
- **prebuilts/manifest-merger**（1）：Bug: 124529986
- **prebuilts/maven_repo**（2）：-
- **prebuilts/misc**（1）：Miscellaneous prebuilt modules
- **prebuilts/module_sdk**（20）：Bug: 237676695
- **prebuilts/ndk**（1）：-
- **prebuilts/ninja**（3）：-
- **prebuilts/python**（3）：-
- **prebuilts/qemu-kernel**（1）：-
- **prebuilts/r8**（1）：Bug: 67880159
- **prebuilts/remoteexecution-client**（1）：Remote Execution Client remoteexecution-client is a tool tha
- **prebuilts/renderscript**（3）：-
- **prebuilts/runtime**（1）：-
- **prebuilts/rust**（1）：Bug: 135215133
- **prebuilts/rust-toolchain**（4）：Bug: 458335153
- **prebuilts/sdk**（1）：-
- **prebuilts/simpleperf**（1）：-
- **prebuilts/swig**（3）：-
- **prebuilts/tools**（1）：-
- **prebuilts/trusty**（1）：Trusty TEE Application SDK This SDK provides the necessary l
- **prebuilts/vndk**（8）：Bug: 111264136
- **sdk**（1）：Development Tools for the SDK
- **superproject**（1）：-
- **superproject/main**（1）：-
- **superproject/main-plus-rust**（1）：-
- **system/acpi**（1）：Bug: 362954346
- **system/adb**（1）：-
- **system/apex**（1）：Bug: 112515528
- **system/ashmemd**（1）：Bug: 123524472
- **system/attestation**（1）：-
- **system/authgraph**（1）：Bug: 293191657
- **system/bluetooth**（1）：bluetooth tools
- **system/bpf**（1）：Bug: 117234388
- **system/bpfprogs**（1）：Bug: 117234388
- **system/bt**（1）：This code has been migrated to platform/packages/modules/Blu
- **system/bvb**（1）：Bug: 27310701
Owner: zeuthen
- **system/ca-certificates**（1）：-
- **system/chre**（1）：Context Hub Runtime Environment (CHRE) This project contains
- **system/connectivity**（5）：-
- **system/core**（1）：minimal bootable environment
- **system/crash_reporter**（1）：crash_reporter crash_reporter is a deamon running on the dev
- **system/cros-codecs**（1）：Cros-codecs A lightweight, simple, low-dependency, and hopef
- **system/dmesgd**（1）：Bug: 217586605
- **system/extras**（1）：debugging/inspection tools
- **system/firewalld**（1）：-
- **system/gatekeeper**（1）：-
- **system/gsid**（1）：Bug: 122471789
- **system/hardware**（1）：-
- **system/hwservicemanager**（1）：-
- **system/incremental_delivery**（1）：Bug: 145679993
- **system/iot**（2）：emmc_image.py is a tool to generate an eMMC USER image. Requ
- **system/keyguard**（1）：-
- **system/keymaster**（1）：-
- **system/keymint**（1）：KeyMint Rust Reference Implementation This repository holds 
- **system/libartpalette**（1）：Bug: 143843616
- **system/libbase**（1）：libbase Who is this library for? This library is a collectio
- **system/libcppbor**（1）：LibCppBor: A Modern C++ CBOR Parser and Generator LibCppBor 
- **system/libfmq**（1）：-
- **system/libhidl**（1）：-
- **system/libhwbinder**（1）：-
- **system/libprocinfo**（1）：Bug: 163786882
- **system/librustutils**（1）：Bug: 195061451
- **system/libsysprop**（1）：Bug: 120044577
- **system/libufdt**（1）：-
- **system/liburingutils**（1）：Bug: 388560452
- **system/libvintf**（1）：-
- **system/libziparchive**（1）：Bug: 149737100
- **system/linkerconfig**（1）：LinkerConfig Introduction Linkerconfig is a program to gener
- **system/logging**（1）：Bug: 168791309
- **system/media**（1）：-
- **system/memory**（8）：Bug: 156383721
- **system/metricsd**（1）：Metricsd The metricsd daemon is used to gather metrics from 
- **system/nativepower**（1）：-
- **system/netd**（1）：-
- **system/nfc**（1）：-
- **system/nvram**（1）：Access-controlled NVRAM implementation This repository conta
- **system/peripheralmanager**（1）：b/26688425
- **system/secretkeeper**（1）：Secretkeeper Secretkeeper provides secure storage of secrets
- **system/secure_element**（1）：Bug: 397456726
- **system/security**（1）：-
- **system/see**（1）：Bug: 350548969
- **system/sepolicy**（1）：Android SEPolicy This directory contains the core Android SE
- **system/server_configurable_flags**（1）：Bug: 118323586
- **system/teeui**（1）：Bug: 139700998
- **system/testing**（1）：Bug: 112605091
- **system/timezone**（1）：-
- **system/tools**（5）：Documentation for this project is currently maintained here:
- **system/tpm**（1）：-
- **system/tpm_manager**（1）：-
- **system/trunks**（1）：-
- **system/ucontainer**（1）：Bug: 116830225
- **system/unwinding**（1）：Bug: 163786882
- **system/update_engine**（1）：Chrome OS Update Process Contents Life of an A/B Update Gene
- **system/usb_info_tools**（1）：Bug: 367203169
- **system/vold**（1）：-
- **system/weaved**（1）：-
- **system/webservd**（1）：-
- **system/wifi**（1）：-
- **system/wlan**（1）：TI 1251 WLAN driver and tools
- **test/AfwTestHarness**（1）：-
- **test/app_compat**（1）：Android App Compatibility Test Suite (C-Suite) C-Suite consi
- **test/catbox**（1）：Bug: 199275786
- **test/cts-root**（1）：Android Compatibility Test Suite - Root extension (CTS-Root)
- **test/dittosuite**（1）：Dittosuite Dittosuite is a collection of tools that simplifi
- **test/framework**（1）：-
- **test/mlts**（2）：Bug: 79732812
- **test/mts**（1）：Android Mainline Test Suite (MTS) MTS consists of a set of t
- **test/robolectric-extensions**（1）：Bug: 282074519
- **test/suite_harness**（1）：Bug: 111264136
- **test/vti**（2）：-
- **test/vts**（1）：-
- **test/vts-testcase**（8）：Bug: 67742483
- **tools/aadevtools**（1）：Android Automotive Developer Tools AADevT contains tools for
- **tools/acloud**（1）：Bug: 70351532
- **tools/adt**（1）：-
- **tools/apifinder**（1）：Bug: 134968344
- **tools/apksig**（1）：apksig apksig is a project which aims to simplify APK signin
- **tools/apkzlib**（1）：Bug: 71699600
- **tools/appbundle**（1）：-
- **tools/asuite**（1）：Bug: 111883332
- **tools/base**（1）：-
- **tools/bdk**（1）：The Brillo Developer Kit (BDK) This is the bdk which is used
- **tools/build**（1）：What is this? The official Gradle plugin to build Android ap
- **tools/buildSrc**（1）：-
- **tools/carrier_settings**（1）：Bug: 162952352
- **tools/content_addressed_storage**（1）：Bug: 286886682
- **tools/currysrc**（1）：Bug: 119806864
- **tools/dctv-tracedb**（1）：What is this thing? DCTV is a trace analysis tool and viewer
- **tools/deviceinfra**（1）：Bug: 301581528
- **tools/dexter**（1）：This is the home of the .dex manipulation library (slicer) a
- **tools/doc_generation**（1）：Bug: 139312525
- **tools/dokka-devsite-plugin**（1）：Bug: 153086942
- **tools/external**（7）：gl | OpenGL Bindings for golang You will need GLEW at least 
- **tools/external_updater**（1）：external_updater external updater is a tool to automatically
- **tools/gpu**（1）：Android gpu tools The android.googlesource.com/platform/tool
- **tools/gradle**（1）：-
- **tools/idea**（1）：-
- **tools/loganalysis**（1）：-
- **tools/metalava**（1）：Metalava Metalava is a metadata generator intended for JVM t
- **tools/motodev**（1）：-
- **tools/ndkports**（1）：ndkports A collection of Android build scripts for various t
- **tools/netsim**（1）：netsim - a network simulation tool for multi-device use case
- **tools/repohooks**（1）：AOSP Preupload Hooks This repo holds hooks that get run by r
- **tools/rr_prebuilt**（1）：rr prebuilts This directory contains the prebuilt binaries f
- **tools/security**（1）：Bug: 77098416
- **tools/studio**（5）：-
- **tools/swt**（1）：-
- **tools/test**（5）：Bug: 74757627
- **tools/tradefederation**（3）：Trade Federation (TF / Tradefed) TF is a test harness used t
- **tools/treble**（1）：Treble https://android-developers.googleblog.com/2017/05/her
- **tools/trebuchet**（1）：Trebuchet Trebuchet is a Kotlin library for parsing and anal
- **vendor/htc**（1）：build configuration for HTC Dream
- **vendor/sample**（1）：-

### kernel（45 个 ok）
- **arcvm-modules/common**（1）：Bug: 230777784
- **build**（1）：Owner: android-kernel-team@google.com
- **build/bootstrap**（1）：Bootstrapping DDKv2 This project contains code to bootstrap 
- **common**（1）：How do I submit patches to Android Common Kernels BEST: Make
- **common-modules/trusty**（1）：Bug: 330795183
- **common-patches**（1）：Android Kernel Common Patches    ---    

Patch series for a
- **configs**（1）：Android Kernel Configs How are kernel config settings typica
- **google-modules/trusty**（1）：Bug: 287695582
- **lk**（1）：The Little Kernel Embedded Operating System The LK kernel is
- **manifest**（1）：Owner: android-kernel-team@google.com
- **prebuilts/4.19**（1）：Bug: 157234803
- **prebuilts/5.10**（2）：Bug: 175581859
- **prebuilts/5.15**（2）：Bug: 205665920
- **prebuilts/5.4**（2）：Bug: 157234803
- **prebuilts/6.1**（2）：Bug: 267772127
- **prebuilts/6.12**（2）：Bug: 381103480
- **prebuilts/6.6**（2）：Bug: 316847414
- **prebuilts/build-tools**（1）：Owner: android-kernel-team@ Bug: 157810926
- **prebuilts/common-modules**（16）：Bug: 387588031
- **prebuilts/mainline**（2）：Bug: 161388412
- **superproject**（1）：Bug: 180542026
- **tests**（1）：Owner: bmahadev@
BUG: 26853153
- **tools/interceptor**（1）：Interceptor WARNING : The interceptor is still a work in pro

### device（186 个 ok）
- **amlogic/yukawa**（1）：Bug: 122486287
- **amlogic/yukawa-kernel**（1）：Bug: 122486287
- **asus/deb**（1）：-
- **asus/flo**（1）：-
- **asus/flo-kernel**（1）：-
- **asus/fugu**（1）：-
- **asus/fugu-kernel**（1）：-
- **asus/grouper**（1）：Files specific to Nexus 7
- **asus/tilapia**（1）：-
- **common**（1）：-
- **freescale/picoimx**（1）：b/26753464
- **generic/arm64**（1）：-
- **generic/armv7-a**（1）：-
- **generic/armv7-a-neon**（1）：-
- **generic/art**（1）：-
- **generic/brillo**（1）：-
- **generic/car**（1）：-
- **generic/common**（1）：GSI This document introduces special GSI settings for facili
- **generic/goldfish**（1）：-
- **generic/goldfish-opengl**（1）：-
- **generic/mini-emulator-arm64**（1）：-
- **generic/mini-emulator-armv7-a-neon**（1）：-
- **generic/mini-emulator-mips**（1）：-
- **generic/mini-emulator-mips64**（1）：-
- **generic/mini-emulator-x86**（1）：-
- **generic/mini-emulator-x86_64**（1）：-
- **generic/mips**（1）：-
- **generic/mips64**（1）：-
- **generic/opengl-transport**（1）：Bug: 114497418
- **generic/trusty**（1）：Bug: 122274911
- **generic/uml**（1）：-
- **generic/vulkan-cereal**（1）：Bug: 128354419
- **generic/x86**（1）：-
- **generic/x86_64**（1）：-
- **google/accessory**（4）：Android accessory support - arduino files.
- **google/akita**（1）：Bug: 334754634
- **google/akita-kernel**（1）：Bug: 334754634
- **google/akita-kernels**（2）：Bug: 357762254
- **google/akita-sepolicy**（1）：Bug: 334754634
- **google/atv**（1）：-
- **google/barbet**（1）：Bug: 190208935
- **google/barbet-kernel**（1）：Bug: 190208935
- **google/barbet-sepolicy**（1）：Bug: 190208935
- **google/bluejay**（1）：Bug: 228757395
- **google/bluejay-kernel**（1）：Bug: 228757395
- **google/bluejay-kernels**（2）：Bug: 357762254
- **google/bluejay-sepolicy**（1）：Bug: 228757395
- **google/bonito**（1）：Bug: 131691077
- **google/bonito-kernel**（1）：Bug: 131691077
- **google/bonito-sepolicy**（1）：Bug: 131691077
- **google/bramble**（1）：Bug: 167236823
- **google/bramble-kernel**（1）：Bug: 167236823
- **google/bramble-sepolicy**（1）：Bug: 167236823
- **google/caimito**（1）：Bug: 343227137
- **google/caimito-kernels**（1）：Bug: 343227137
- **google/caimito-sepolicy**（1）：Bug: 343227137
- **google/comet**（1）：Bug: 355405604
- **google/comet-kernels**（1）：Bug: 355405604
- **google/comet-sepolicy**（1）：Bug: 355405604
- **google/contexthub**（1）：-
- **google/coral**（1）：Bug: 141248619
- **google/coral-kernel**（1）：Bug: 141248619
- **google/coral-sepolicy**（1）：Bug: 141248619
- **google/crosshatch**（1）：Bug: 115885826
- **google/crosshatch-kernel**（1）：Bug: 115885826
- **google/crosshatch-sepolicy**（1）：Bug: 115885826
- **google/cuttlefish**（1）：Note For all host tools development please refer to https://
- **google/cuttlefish_prebuilts**（1）：Bug: 162963599
- **google/cuttlefish_vmm**（1）：Bug: 122613967
- **google/debugcable**（1）：-
- **google/dragon**（1）：-
- **google/dragon-kernel**（1）：-
- **google/felix**（1）：Bug: 277833819
- **google/felix-kernel**（1）：Bug: 277833819
- **google/felix-kernels**（2）：Bug: 357762254
- **google/felix-sepolicy**（1）：Bug: 277833819
- **google/fuchsia**（1）：Fuchsia targets TODO
- **google/gs-common**（1）：Bug: 201551519
- **google/gs101**（1）：Bug: 201551519
- **google/gs101-sepolicy**（1）：Bug: 201551519
- **google/gs201**（1）：Bug: 244231765
- **google/gs201-sepolicy**（1）：Bug: 244231765
- **google/lynx**（1）：Bug: 277736560
- **google/lynx-kernel**（1）：Bug: 277736560
- **google/lynx-kernels**（2）：Bug: 357762254
- **google/lynx-sepolicy**（1）：Bug: 277736560
- **google/marlin**（1）：-
- **google/marlin-kernel**（1）：-
- **google/muskie**（1）：-
- **google/pantah**（1）：Bug: 244231765
- **google/pantah-kernel**（1）：Bug: 244231765
- **google/pantah-kernels**（2）：Bug: 357762254
- **google/pantah-sepolicy**（1）：Bug: 244231765
- **google/raviole**（1）：Bug: 201551519
- **google/raviole-kernel**（1）：Bug: 201551519
- **google/raviole-kernels**（2）：Bug: 357762254
- **google/redbull**（1）：Bug: 167236823
- **google/redbull-kernel**（1）：Bug: 179089302
- **google/redbull-sepolicy**（1）：Bug: 167236823
- **google/redfin**（1）：Bug: 167236823
- **google/redfin-kernel**（1）：Bug: 167236823
- **google/redfin-sepolicy**（1）：Bug: 167236823
- **google/shusky**（1）：Bug: 299982256
- **google/shusky-kernel**（1）：Bug: 299982256
- **google/shusky-kernels**（2）：Bug: 357762254
- **google/shusky-sepolicy**（1）：Bug: 299982256
- **google/sunfish**（1）：Bug: 160260413
- **google/sunfish-kernel**（1）：Bug: 160260413
- **google/sunfish-sepolicy**（1）：Bug: 160260413
- **google/taimen**（1）：-
- **google/tangorpro**（1）：Bug: 273801859
- **google/tangorpro-kernel**（1）：Bug: 273801859
- **google/tangorpro-kernels**（2）：Bug: 357762254
- **google/tangorpro-sepolicy**（1）：Bug: 273801859
- **google/trout**（1）：Bug: 162952352
- **google/vrservices**（1）：-
- **google/wahoo**（1）：-
- **google/wahoo-kernel**（1）：-
- **google/zuma**（1）：Bug: 299982256
- **google/zuma-sepolicy**（1）：Bug: 299982256
- **google/zumapro**（1）：Bug: 343227137
- **google/zumapro-sepolicy**（1）：Bug: 343227137
- **google_car**（1）：Bug: 139539411
- **htc/common**（1）：Files specific to HTC devices but shared between multiple HT
- **htc/dream**（1）：Files specific to HTC dream hardware
- **htc/dream-sapphire**（1）：-
- **htc/flounder**（1）：-
- **htc/flounder-kernel**（1）：-
- **htc/passion**（1）：Files specific to HTC passion hardware
- **htc/passion-common**（1）：Files specific to HTC passion hardware
- **htc/sapphire**（1）：Files specific to HTC sapphire hardware
- **huawei/angler**（1）：-
- **huawei/angler-kernel**（1）：-
- **imagination/creatorci41**（1）：b/26880144
- **intel/edison**（1）：-
- **intel/minnowboard**（1）：b/26729241
- **lge/bullhead**（1）：-
- **lge/bullhead-kernel**（1）：-
- **lge/hammerhead**（1）：-
- **lge/hammerhead-kernel**（1）：-
- **lge/mako**（1）：-
- **lge/mako-kernel**（1）：-
- **linaro/bootloader**（3）：-
- **linaro/dragonboard**（1）：Bug: 140122761
- **linaro/dragonboard-kernel**（1）：Bug: 140122761
- **linaro/hikey**（1）：-
- **linaro/hikey-kernel**（1）：-
- **linaro/poplar**（1）：Bug: 110789980
- **linaro/poplar-kernel**（1）：Bug: 110789980
- **marvell/abox_edge**（1）：b/26407117
- **mediatek/wembley-sepolicy**（1）：Bug: 162952352
- **moto/common**（1）：-
- **moto/shamu**（1）：-
- **moto/shamu-kernel**（1）：-
- **moto/stingray**（1）：-
- **moto/wingray**（1）：-
- **qcom/dragonboard**（1）：-
- **rockchip/kylin**（1）：b/26753464
- **sample**（1）：-
- **samsung/crespo**（1）：Files specific to Samsung crespo hardware, a.k.a. Nexus S.
- **samsung/crespo4g**（1）：Files specific to Samsung crespo4g hardware, a.k.a. Nexus S 
- **samsung/maguro**（1）：-
- **samsung/manta**（1）：-
- **samsung/toro**（1）：-
- **samsung/toroplus**（1）：Files related to toroplus, i.e. the Sprint Galaxy Nexus.
- **samsung/torospr**（1）：-
- **samsung/tuna**（1）：-
- **samsung_slsi/arndale**（1）：-
- **sony/lt26**（1）：Files specific to the Sony LT26 ("Xperia S")
- **ti/beagle-x15**（1）：Bug: 111362717
- **ti/beagle-x15-kernel**（1）：Bug: 111362717
- **ti/bootloader**（1）：-
- **ti/panda**（1）：-

### toolchain（80 个 ok）
- **android_rust**（1）：Android Rust Toolchain For the latest version of this doc, p
- **avr-libc**（1）：-
- **benchmark**（1）：-
- **binutils**（1）：-
- **build**（1）：-
- **capnproto**（1）：Cap‘n Proto is an insanely fast data interchange format and 
- **cargo-deny**（1）：❌ cargo-deny Cargo plugin for linting your dependencies See 
- **cargo-vet**（1）：cargo-vet The cargo vet subcommand is a tool to help project
- **ccache**（1）：-
- **clang**（1）：-
- **clang-tools-extra**（1）：-
- **cloog**（1）：-
- **compiler-rt**（1）：-
- **expat**（1）：-
- **gcc**（1）：Building GCC for Android The following process is used to bu
- **gdb**（1）：-
- **gmp**（1）：-
- **go**（1）：The Go Programming Language Go is an open source programming
- **isl**（1）：-
- **jdk/build**（1）：-
- **jdk/jdk11**（1）：Bug: 137656389
- **jdk/jdk17**（1）：Welcome to the JDK! For build instructions please see the on
- **jdk/jdk21**（1）：Welcome to the JDK! For build instructions please see the on
- **jdk/jdk25**（1）：Welcome to the JDK! For build instructions please see the on
- **jdk/jdk9**（1）：Bug: 62123342
- **jdk/jdk9_corba**（1）：Bug: 62123342
- **jdk/jdk9_hotspot**（1）：Bug: 62123342
- **jdk/jdk9_jaxp**（1）：Bug: 62123342
- **jdk/jdk9_jaxws**（1）：Bug: 62123342
- **jdk/jdk9_jdk**（1）：Bug: 62123342
- **jdk/jdk9_langtools**（1）：Bug: 62123342
- **jdk/jdk9_nashorn**（1）：Bug: 62123342
- **libcxx**（1）：-
- **libcxxabi**（1）：-
- **lld**（1）：LLVM Linker (lld) This directory and its subdirectories cont
- **llvm**（1）：-
- **llvm-project**（1）：The LLVM Compiler Infrastructure Welcome to the LLVM project
- **llvm_android**（1）：Android Clang/LLVM Toolchain Quick links: Android clang buil
- **m4**（1）：Bug: 117243010
- **make**（1）：Bug: 117241963
- **manifest**（1）：-
- **mclinker**（1）：-
- **mingw**（1）：Building Mingw for Android The build.sh script in this direc
- **mpc**（1）：-
- **mpfr**（1）：-
- **ndk-kokoro**（1）：Bug: 200122552
- **ndk_chromite_config**（1）：-
- **openmp_llvm**（1）：-
- **perl**（1）：-
- **pgo-profiles**（1）：Bug: 72041779
- **ppl**（1）：-
- **prebuilts/ndk**（15）：Android NDK Documentation NDK documentation, guides, and API
- **prebuilts/ndk-darwin**（4）：Android NDK Documentation NDK documentation, guides, and API
- **prebuilts/sysroot**（1）：Bug: 255592883
- **python**（1）：-
- **riscv_gnu_toolchain**（1）：RISC-V GNU Compiler Toolchain This is the RISC-V C and C++ c
- **rr**（1）：Overview rr is a lightweight tool for recording, replaying a
- **rustc**（1）：Website | Getting started | Learn | Documentation | Contribu
- **sccache**（1）：sccache - Shared Compilation Cache sccache is a ccache -like
- **sed**（1）：-
- **superproject**（1）：-
- **xz**（1）：-
- **yasm**（1）：-

### trusty（36 个 ok）
- **app/authmgr**（1）：Bug: 371226688
- **app/avb**（1）：AVB resource manager The AVB ( Android Verified Boot ) resou
- **app/cast-auth**（1）：Bug: 219098067
- **app/confirmationui**（1）：ConfirmationUI Trusted App This is an implementation of the 
- **app/gatekeeper**（1）：-
- **app/keymaster**（1）：-
- **app/keymint**（1）：Bug: 223458328
- **app/nvram**（1）：Access-controlled NVRAM app for Trusty This repository conta
- **app/sample**（1）：-
- **app/secretkeeper**（1）：Bug: 310885032
- **app/storage**（1）：Secure storage service The secure storage service provides e
- **device/arm**（2）：-
- **device/common**（1）：Bug: 390682260
- **device/desktop**（1）：Bug: 361072469
- **device/nxp**（2）：-
- **device/x86**（1）：Bug: 113605827
- **external/headers**（1）：-
- **external/musl**（1）：Bug: 131239750
- **external/qemu**（1）：-
- **external/qemu-keycodemapdb**（1）：Bug: 112114220
- **external/trusted-firmware-a**（1）：Bug: 127811687
- **external/trusty**（1）：-
- **host/aidl**（1）：Documentation for this project is currently maintained here:
- **host/common**（1）：Bug: 234928363
- **lib**（1）：-
- **lk/common**（1）：LK The LK embedded kernel. An SMP-aware kernel designed for 
- **lk/nxp**（1）：-
- **lk/trusty**（1）：-
- **manifest**（1）：-
- **prebuilts/aosp**（1）：Bug: 123422629
- **superproject**（1）：-
- **trusty**（1）：For ACL only
- **user/desktop**（1）：Bug: 361072469
- **vendor/google**（1）：-

## 4. 受限/不可访问仓库
- Kernel-Projects
- Platform-Chromium-Projects
- Platform-Projects
- Platform-Unrestricted-Projects
- Public-Projects
- cts_drno_filter
- external/rust/crates/aarch64-cpu
- external/rust/crates/autocfg
- kernel/google-modules/wlan/qcom/wcn6740/cnss2
- kernel/hikey-linaro
- kkernel/prebuilts/common-modules/virtual-device/mainline/arm64
- pdk_review_filter
- platform/brillo
- platform/external/toy
- platform/external/vtable-dumper
- platform/packages/modules/MediaSwCodec
- platform/packages/modules/PermissionController
- platform/system/libueventd-rs
- platform/system/software_defined_vehicle/vpm
- platform/tools/google_prebuilts/studio/sdk/remote
- platform/tools/rootcanal

## 5. 待补爬仓库（retry/pending）