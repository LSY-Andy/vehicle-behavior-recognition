IN_DATA_DIR="./video_crop"
OUT_DATA_DIR="./frames"

if [[ ! -d "${OUT_DATA_DIR}" ]]; then
  echo "${OUT_DATA_DIR} doesn't exist. Creating it.";
  mkdir -p ${OUT_DATA_DIR}
fi

for video in $(ls -A1 -U ${IN_DATA_DIR}/*)
do
  video_name=${video##*/}

  echo $video_name
#   array=(${video_name//./}) 将所有MP4都改成空
  array=(${video_name//.mp4/})
  video_name=${array[0]}
  echo $video_name
    

  out_video_dir=${OUT_DATA_DIR}/${video_name}/
  mkdir -p "${out_video_dir}"

  out_name="${out_video_dir}/${video_name}_%06d.jpg"

  ffmpeg -i "${video}" -r 30 -q:v 1 "${out_name}"

done
# String[] cmd = {"-i","${video}","-r 30","-q:v 1","${out_name}"}
# String[] commands = new String[10];
# commands[0] ="-i";
# commands[1] = "${video}";
# commands[2] ="-r 30"
# commands[3] ="-q:v 1"
# commands[4] ="" 