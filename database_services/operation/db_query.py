insert_song = "INSERT INTO music_files( song_id, song_name, song_duration, upload_time) VALUES  (%r,%r,%d,%r)"
insert_podcast = "INSERT INTO podcast_records( podcast_id, podcast_name, podcast_host, podcast_duration, participants_1, participants_2, participants_3, participants_4, participants_5, participants_6, participants_7, participants_8, participants_9, participants_10, podcast_time) VALUES  (%r,%r,%r,%d,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r,%r)"
insert_audiobook = "INSERT INTO audiobook_library( audiobook_id, audiobook_title, audiobook_author, audiobook_narrator, audiobook_duration, upload_time) VALUES  (%r,%r,%r,%r,%d,%r)"

update_song = "UPDATE music_files SET song_name=%r, song_duration=%d, upload_time=%r WHERE song_id=%r"
update_podcast = "UPDATE podcast_records SET podcast_name=%r, podcast_host=%r, podcast_duration=%d, participants_1=%r, participants_2=%r, participants_3=%r, participants_4=%r, participants_5=%r, participants_6=%r, participants_7=%r, participants_8=%r, participants_9=%r, participants_10=%r, podcast_time=%r WHERE podcast_id=%r"
update_audiobook = "UPDATE audiobook_library SET audiobook_title=%r, audiobook_author=%r, audiobook_narrator=%r, audiobook_duration=%d, upload_time=%r WHERE audiobook_id=%r"


delete_song = "DELETE FROM music_files WHERE song_id=%r "
delete_podcast = "DELETE FROM podcast_records WHERE podcast_id = %r "
delete_audiobook = "DELETE FROM audiobook_library WHERE audiobook_id=%r "

fetch_song = "SELECT song_name FROM music_files WHERE song_id=%r"
fetch_podcast = "SELECT podcast_name FROM podcast_records WHERE podcast_id=%r"
fetch_audiobook = "SELECT audiobook_title FROM audiobook_library WHERE audiobook_id=%r"

fetchall_song = "SELECT song_name FROM music_files"
fetchall_podcast = "SELECT podcast_name FROM podcast_records"
fetchall_audiobook = "SELECT audiobook_title FROM audiobook_library"