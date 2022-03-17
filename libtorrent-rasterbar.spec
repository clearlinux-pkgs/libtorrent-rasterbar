#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libtorrent-rasterbar
Version  : 2.0.5
Release  : 8
URL      : https://github.com/arvidn/libtorrent/releases/download/v2.0.5/libtorrent-rasterbar-2.0.5.tar.gz
Source0  : https://github.com/arvidn/libtorrent/releases/download/v2.0.5/libtorrent-rasterbar-2.0.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause BSL-1.0 GPL-3.0
Requires: libtorrent-rasterbar-data = %{version}-%{release}
Requires: libtorrent-rasterbar-lib = %{version}-%{release}
Requires: libtorrent-rasterbar-license = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : glibc-dev
BuildRequires : openssl-dev
BuildRequires : pkg-config
BuildRequires : python3-dev

%description
.. image:: docs/img/logo-color-text.png
.. image:: https://github.com/arvidn/libtorrent/actions/workflows/windows.yml/badge.svg
:target: https://github.com/arvidn/libtorrent/actions/workflows/windows.yml

%package data
Summary: data components for the libtorrent-rasterbar package.
Group: Data

%description data
data components for the libtorrent-rasterbar package.


%package dev
Summary: dev components for the libtorrent-rasterbar package.
Group: Development
Requires: libtorrent-rasterbar-lib = %{version}-%{release}
Requires: libtorrent-rasterbar-data = %{version}-%{release}
Provides: libtorrent-rasterbar-devel = %{version}-%{release}
Requires: libtorrent-rasterbar = %{version}-%{release}

%description dev
dev components for the libtorrent-rasterbar package.


%package lib
Summary: lib components for the libtorrent-rasterbar package.
Group: Libraries
Requires: libtorrent-rasterbar-data = %{version}-%{release}
Requires: libtorrent-rasterbar-license = %{version}-%{release}

%description lib
lib components for the libtorrent-rasterbar package.


%package license
Summary: license components for the libtorrent-rasterbar package.
Group: Default

%description license
license components for the libtorrent-rasterbar package.


%prep
%setup -q -n libtorrent-rasterbar-2.0.5
cd %{_builddir}/libtorrent-rasterbar-2.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1647493152
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1647493152
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libtorrent-rasterbar
cp %{_builddir}/libtorrent-rasterbar-2.0.5/COPYING %{buildroot}/usr/share/package-licenses/libtorrent-rasterbar/bcb19528a41eea29d37cc740bb78a041314ecdb7
cp %{_builddir}/libtorrent-rasterbar-2.0.5/deps/asio-gnutls/LICENSE_1_0.txt %{buildroot}/usr/share/package-licenses/libtorrent-rasterbar/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/libtorrent-rasterbar-2.0.5/deps/try_signal/LICENSE %{buildroot}/usr/share/package-licenses/libtorrent-rasterbar/780a263c476ddbf4f51b12f82855201f7839a4a3
cp %{_builddir}/libtorrent-rasterbar-2.0.5/simulation/libsimulator/LICENSE %{buildroot}/usr/share/package-licenses/libtorrent-rasterbar/db0f086d1ffc769d49c9f98b18643a11c2fb7972
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/libtorrent/add_torrent_params.hpp
/usr/include/libtorrent/address.hpp
/usr/include/libtorrent/alert.hpp
/usr/include/libtorrent/alert_types.hpp
/usr/include/libtorrent/announce_entry.hpp
/usr/include/libtorrent/assert.hpp
/usr/include/libtorrent/aux_/alert_manager.hpp
/usr/include/libtorrent/aux_/aligned_storage.hpp
/usr/include/libtorrent/aux_/aligned_union.hpp
/usr/include/libtorrent/aux_/alloca.hpp
/usr/include/libtorrent/aux_/allocating_handler.hpp
/usr/include/libtorrent/aux_/announce_entry.hpp
/usr/include/libtorrent/aux_/apply_pad_files.hpp
/usr/include/libtorrent/aux_/array.hpp
/usr/include/libtorrent/aux_/bandwidth_limit.hpp
/usr/include/libtorrent/aux_/bandwidth_manager.hpp
/usr/include/libtorrent/aux_/bandwidth_queue_entry.hpp
/usr/include/libtorrent/aux_/bandwidth_socket.hpp
/usr/include/libtorrent/aux_/bind_to_device.hpp
/usr/include/libtorrent/aux_/buffer.hpp
/usr/include/libtorrent/aux_/byteswap.hpp
/usr/include/libtorrent/aux_/chained_buffer.hpp
/usr/include/libtorrent/aux_/container_wrapper.hpp
/usr/include/libtorrent/aux_/cpuid.hpp
/usr/include/libtorrent/aux_/deferred_handler.hpp
/usr/include/libtorrent/aux_/deprecated.hpp
/usr/include/libtorrent/aux_/deque.hpp
/usr/include/libtorrent/aux_/dev_random.hpp
/usr/include/libtorrent/aux_/directory.hpp
/usr/include/libtorrent/aux_/disable_deprecation_warnings_push.hpp
/usr/include/libtorrent/aux_/disable_warnings_pop.hpp
/usr/include/libtorrent/aux_/disable_warnings_push.hpp
/usr/include/libtorrent/aux_/disk_buffer_pool.hpp
/usr/include/libtorrent/aux_/disk_io_job.hpp
/usr/include/libtorrent/aux_/disk_io_thread_pool.hpp
/usr/include/libtorrent/aux_/disk_job_fence.hpp
/usr/include/libtorrent/aux_/disk_job_pool.hpp
/usr/include/libtorrent/aux_/ed25519.hpp
/usr/include/libtorrent/aux_/escape_string.hpp
/usr/include/libtorrent/aux_/export.hpp
/usr/include/libtorrent/aux_/ffs.hpp
/usr/include/libtorrent/aux_/file_pointer.hpp
/usr/include/libtorrent/aux_/file_progress.hpp
/usr/include/libtorrent/aux_/file_view_pool.hpp
/usr/include/libtorrent/aux_/generate_peer_id.hpp
/usr/include/libtorrent/aux_/has_block.hpp
/usr/include/libtorrent/aux_/hasher512.hpp
/usr/include/libtorrent/aux_/heterogeneous_queue.hpp
/usr/include/libtorrent/aux_/instantiate_connection.hpp
/usr/include/libtorrent/aux_/invariant_check.hpp
/usr/include/libtorrent/aux_/io.hpp
/usr/include/libtorrent/aux_/ip_helpers.hpp
/usr/include/libtorrent/aux_/ip_notifier.hpp
/usr/include/libtorrent/aux_/keepalive.hpp
/usr/include/libtorrent/aux_/listen_socket_handle.hpp
/usr/include/libtorrent/aux_/lsd.hpp
/usr/include/libtorrent/aux_/merkle.hpp
/usr/include/libtorrent/aux_/merkle_tree.hpp
/usr/include/libtorrent/aux_/mmap.hpp
/usr/include/libtorrent/aux_/noexcept_movable.hpp
/usr/include/libtorrent/aux_/numeric_cast.hpp
/usr/include/libtorrent/aux_/open_mode.hpp
/usr/include/libtorrent/aux_/packet_buffer.hpp
/usr/include/libtorrent/aux_/packet_pool.hpp
/usr/include/libtorrent/aux_/path.hpp
/usr/include/libtorrent/aux_/polymorphic_socket.hpp
/usr/include/libtorrent/aux_/pool.hpp
/usr/include/libtorrent/aux_/portmap.hpp
/usr/include/libtorrent/aux_/posix_part_file.hpp
/usr/include/libtorrent/aux_/posix_storage.hpp
/usr/include/libtorrent/aux_/proxy_settings.hpp
/usr/include/libtorrent/aux_/range.hpp
/usr/include/libtorrent/aux_/receive_buffer.hpp
/usr/include/libtorrent/aux_/resolver.hpp
/usr/include/libtorrent/aux_/resolver_interface.hpp
/usr/include/libtorrent/aux_/route.h
/usr/include/libtorrent/aux_/scope_end.hpp
/usr/include/libtorrent/aux_/session_call.hpp
/usr/include/libtorrent/aux_/session_impl.hpp
/usr/include/libtorrent/aux_/session_interface.hpp
/usr/include/libtorrent/aux_/session_settings.hpp
/usr/include/libtorrent/aux_/session_udp_sockets.hpp
/usr/include/libtorrent/aux_/set_socket_buffer.hpp
/usr/include/libtorrent/aux_/sha512.hpp
/usr/include/libtorrent/aux_/socket_type.hpp
/usr/include/libtorrent/aux_/storage_free_list.hpp
/usr/include/libtorrent/aux_/storage_utils.hpp
/usr/include/libtorrent/aux_/store_buffer.hpp
/usr/include/libtorrent/aux_/string_ptr.hpp
/usr/include/libtorrent/aux_/strview_less.hpp
/usr/include/libtorrent/aux_/suggest_piece.hpp
/usr/include/libtorrent/aux_/throw.hpp
/usr/include/libtorrent/aux_/time.hpp
/usr/include/libtorrent/aux_/timestamp_history.hpp
/usr/include/libtorrent/aux_/torrent_impl.hpp
/usr/include/libtorrent/aux_/torrent_list.hpp
/usr/include/libtorrent/aux_/unique_ptr.hpp
/usr/include/libtorrent/aux_/utp_socket_manager.hpp
/usr/include/libtorrent/aux_/utp_stream.hpp
/usr/include/libtorrent/aux_/vector.hpp
/usr/include/libtorrent/aux_/win_cng.hpp
/usr/include/libtorrent/aux_/win_crypto_provider.hpp
/usr/include/libtorrent/aux_/win_util.hpp
/usr/include/libtorrent/aux_/windows.hpp
/usr/include/libtorrent/bdecode.hpp
/usr/include/libtorrent/bencode.hpp
/usr/include/libtorrent/bitfield.hpp
/usr/include/libtorrent/bloom_filter.hpp
/usr/include/libtorrent/bt_peer_connection.hpp
/usr/include/libtorrent/choker.hpp
/usr/include/libtorrent/client_data.hpp
/usr/include/libtorrent/close_reason.hpp
/usr/include/libtorrent/config.hpp
/usr/include/libtorrent/copy_ptr.hpp
/usr/include/libtorrent/crc32c.hpp
/usr/include/libtorrent/create_torrent.hpp
/usr/include/libtorrent/deadline_timer.hpp
/usr/include/libtorrent/debug.hpp
/usr/include/libtorrent/disabled_disk_io.hpp
/usr/include/libtorrent/disk_buffer_holder.hpp
/usr/include/libtorrent/disk_interface.hpp
/usr/include/libtorrent/disk_observer.hpp
/usr/include/libtorrent/download_priority.hpp
/usr/include/libtorrent/entry.hpp
/usr/include/libtorrent/enum_net.hpp
/usr/include/libtorrent/error.hpp
/usr/include/libtorrent/error_code.hpp
/usr/include/libtorrent/extensions.hpp
/usr/include/libtorrent/extensions/smart_ban.hpp
/usr/include/libtorrent/extensions/ut_metadata.hpp
/usr/include/libtorrent/extensions/ut_pex.hpp
/usr/include/libtorrent/file.hpp
/usr/include/libtorrent/file_storage.hpp
/usr/include/libtorrent/fingerprint.hpp
/usr/include/libtorrent/flags.hpp
/usr/include/libtorrent/fwd.hpp
/usr/include/libtorrent/gzip.hpp
/usr/include/libtorrent/hash_picker.hpp
/usr/include/libtorrent/hasher.hpp
/usr/include/libtorrent/hex.hpp
/usr/include/libtorrent/http_connection.hpp
/usr/include/libtorrent/http_parser.hpp
/usr/include/libtorrent/http_seed_connection.hpp
/usr/include/libtorrent/http_stream.hpp
/usr/include/libtorrent/http_tracker_connection.hpp
/usr/include/libtorrent/i2p_stream.hpp
/usr/include/libtorrent/identify_client.hpp
/usr/include/libtorrent/index_range.hpp
/usr/include/libtorrent/info_hash.hpp
/usr/include/libtorrent/io.hpp
/usr/include/libtorrent/io_context.hpp
/usr/include/libtorrent/io_service.hpp
/usr/include/libtorrent/ip_filter.hpp
/usr/include/libtorrent/ip_voter.hpp
/usr/include/libtorrent/kademlia/announce_flags.hpp
/usr/include/libtorrent/kademlia/dht_observer.hpp
/usr/include/libtorrent/kademlia/dht_settings.hpp
/usr/include/libtorrent/kademlia/dht_state.hpp
/usr/include/libtorrent/kademlia/dht_storage.hpp
/usr/include/libtorrent/kademlia/dht_tracker.hpp
/usr/include/libtorrent/kademlia/direct_request.hpp
/usr/include/libtorrent/kademlia/dos_blocker.hpp
/usr/include/libtorrent/kademlia/ed25519.hpp
/usr/include/libtorrent/kademlia/find_data.hpp
/usr/include/libtorrent/kademlia/get_item.hpp
/usr/include/libtorrent/kademlia/get_peers.hpp
/usr/include/libtorrent/kademlia/io.hpp
/usr/include/libtorrent/kademlia/item.hpp
/usr/include/libtorrent/kademlia/msg.hpp
/usr/include/libtorrent/kademlia/node.hpp
/usr/include/libtorrent/kademlia/node_entry.hpp
/usr/include/libtorrent/kademlia/node_id.hpp
/usr/include/libtorrent/kademlia/observer.hpp
/usr/include/libtorrent/kademlia/put_data.hpp
/usr/include/libtorrent/kademlia/refresh.hpp
/usr/include/libtorrent/kademlia/routing_table.hpp
/usr/include/libtorrent/kademlia/rpc_manager.hpp
/usr/include/libtorrent/kademlia/sample_infohashes.hpp
/usr/include/libtorrent/kademlia/traversal_algorithm.hpp
/usr/include/libtorrent/kademlia/types.hpp
/usr/include/libtorrent/libtorrent.hpp
/usr/include/libtorrent/link.hpp
/usr/include/libtorrent/lsd.hpp
/usr/include/libtorrent/magnet_uri.hpp
/usr/include/libtorrent/mmap_disk_io.hpp
/usr/include/libtorrent/mmap_storage.hpp
/usr/include/libtorrent/natpmp.hpp
/usr/include/libtorrent/netlink.hpp
/usr/include/libtorrent/operations.hpp
/usr/include/libtorrent/optional.hpp
/usr/include/libtorrent/parse_url.hpp
/usr/include/libtorrent/part_file.hpp
/usr/include/libtorrent/pe_crypto.hpp
/usr/include/libtorrent/peer.hpp
/usr/include/libtorrent/peer_class.hpp
/usr/include/libtorrent/peer_class_set.hpp
/usr/include/libtorrent/peer_class_type_filter.hpp
/usr/include/libtorrent/peer_connection.hpp
/usr/include/libtorrent/peer_connection_handle.hpp
/usr/include/libtorrent/peer_connection_interface.hpp
/usr/include/libtorrent/peer_id.hpp
/usr/include/libtorrent/peer_info.hpp
/usr/include/libtorrent/peer_list.hpp
/usr/include/libtorrent/peer_request.hpp
/usr/include/libtorrent/performance_counters.hpp
/usr/include/libtorrent/pex_flags.hpp
/usr/include/libtorrent/piece_block.hpp
/usr/include/libtorrent/piece_block_progress.hpp
/usr/include/libtorrent/piece_picker.hpp
/usr/include/libtorrent/platform_util.hpp
/usr/include/libtorrent/portmap.hpp
/usr/include/libtorrent/posix_disk_io.hpp
/usr/include/libtorrent/proxy_base.hpp
/usr/include/libtorrent/puff.hpp
/usr/include/libtorrent/random.hpp
/usr/include/libtorrent/read_resume_data.hpp
/usr/include/libtorrent/request_blocks.hpp
/usr/include/libtorrent/resolve_links.hpp
/usr/include/libtorrent/session.hpp
/usr/include/libtorrent/session_handle.hpp
/usr/include/libtorrent/session_params.hpp
/usr/include/libtorrent/session_settings.hpp
/usr/include/libtorrent/session_stats.hpp
/usr/include/libtorrent/session_status.hpp
/usr/include/libtorrent/session_types.hpp
/usr/include/libtorrent/settings_pack.hpp
/usr/include/libtorrent/sha1.hpp
/usr/include/libtorrent/sha1_hash.hpp
/usr/include/libtorrent/sha256.hpp
/usr/include/libtorrent/sliding_average.hpp
/usr/include/libtorrent/socket.hpp
/usr/include/libtorrent/socket_io.hpp
/usr/include/libtorrent/socket_type.hpp
/usr/include/libtorrent/socks5_stream.hpp
/usr/include/libtorrent/span.hpp
/usr/include/libtorrent/ssl.hpp
/usr/include/libtorrent/ssl_stream.hpp
/usr/include/libtorrent/stack_allocator.hpp
/usr/include/libtorrent/stat.hpp
/usr/include/libtorrent/stat_cache.hpp
/usr/include/libtorrent/storage.hpp
/usr/include/libtorrent/storage_defs.hpp
/usr/include/libtorrent/string_util.hpp
/usr/include/libtorrent/string_view.hpp
/usr/include/libtorrent/tailqueue.hpp
/usr/include/libtorrent/time.hpp
/usr/include/libtorrent/torrent.hpp
/usr/include/libtorrent/torrent_flags.hpp
/usr/include/libtorrent/torrent_handle.hpp
/usr/include/libtorrent/torrent_info.hpp
/usr/include/libtorrent/torrent_peer.hpp
/usr/include/libtorrent/torrent_peer_allocator.hpp
/usr/include/libtorrent/torrent_status.hpp
/usr/include/libtorrent/tracker_manager.hpp
/usr/include/libtorrent/udp_socket.hpp
/usr/include/libtorrent/udp_tracker_connection.hpp
/usr/include/libtorrent/union_endpoint.hpp
/usr/include/libtorrent/units.hpp
/usr/include/libtorrent/upnp.hpp
/usr/include/libtorrent/utf8.hpp
/usr/include/libtorrent/vector_utils.hpp
/usr/include/libtorrent/version.hpp
/usr/include/libtorrent/web_connection_base.hpp
/usr/include/libtorrent/web_peer_connection.hpp
/usr/include/libtorrent/write_resume_data.hpp
/usr/include/libtorrent/xml_parse.hpp
/usr/lib64/cmake/LibtorrentRasterbar/LibtorrentRasterbarConfig.cmake
/usr/lib64/cmake/LibtorrentRasterbar/LibtorrentRasterbarConfigVersion.cmake
/usr/lib64/cmake/LibtorrentRasterbar/LibtorrentRasterbarTargets-relwithdebinfo.cmake
/usr/lib64/cmake/LibtorrentRasterbar/LibtorrentRasterbarTargets.cmake
/usr/lib64/libtorrent-rasterbar.so
/usr/lib64/pkgconfig/libtorrent-rasterbar.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtorrent-rasterbar.so.2.0
/usr/lib64/libtorrent-rasterbar.so.2.0.5

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libtorrent-rasterbar/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/libtorrent-rasterbar/780a263c476ddbf4f51b12f82855201f7839a4a3
/usr/share/package-licenses/libtorrent-rasterbar/bcb19528a41eea29d37cc740bb78a041314ecdb7
/usr/share/package-licenses/libtorrent-rasterbar/db0f086d1ffc769d49c9f98b18643a11c2fb7972
